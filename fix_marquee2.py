#!/usr/bin/env python3
"""
Surgery script 2: Remove old /sliding/ logo strip that uses different class names.
"""
import re, shutil

SRC = '/var/www/mgbwgroup-static/index.html'
BAK2 = '/var/www/mgbwgroup-static/index.html.bak_marquee2'

html = open(SRC).read()
print(f"File: {len(html)} chars")

shutil.copy2(SRC, BAK2)
print(f"Backup: {BAK2}")

# Find the /sliding/ logo section
# It uses srcset="/sliding/ paths
sliding_positions = [m.start() for m in re.finditer(r'/sliding/', html)]
print(f"Found {len(sliding_positions)} /sliding/ refs at: {sliding_positions}")

if not sliding_positions:
    print("No /sliding/ paths found. Nothing to do.")
    exit(0)

first_sliding = sliding_positions[0]
last_sliding = sliding_positions[-1]

# Need to find the wrapper section/div around all these sliding images
# Walk backward from first occurrence to find <section or major <div wrapper
search_back = max(0, first_sliding - 3000)
chunk_before = html[search_back:first_sliding]

# Look for section opens
section_opens = [(search_back + m.start(), m.group()) for m in re.finditer(r'<section[^>]*>', chunk_before)]
print(f"Section opens before sliding logos: {[(p, t[:60]) for p,t in section_opens]}")

# Look for div opens that might be the outer wrapper
# The sliding logos seem to be inside a flex container

# After the last sliding reference, find closing tags
search_forward_start = last_sliding
search_forward_end = min(len(html), last_sliding + 1000)
chunk_after = html[search_forward_start:search_forward_end]

# Find where the sliding section ends - look for </div></div></div> pattern followed by <section (new marquee)
# From the zoomed screenshot: ...></div></div></div></div>\n<section class="w-full py-10" style="background:#f8f0fc
end_pattern = re.search(r'</div>\s*</div>\s*</div>\s*</div>\s*\n?<section class="w-full py-10"', chunk_after)
if end_pattern:
    section_end = search_forward_start + end_pattern.start()
    # Count the closing divs to find where the sliding section wrapper ends
    # The end is at the last </div> before the new marquee <section>
    closing_divs_end = search_forward_start + end_pattern.start()
    # Find position of the \n<section to know exactly where divs end
    new_section_start = html.find('<section class="w-full py-10"', last_sliding)
    if new_section_start > 0:
        # Everything between? Let's find the wrapper start
        # Walk back from first_sliding to find the opening of this logo block
        # Look for a pattern like overflow:hidden or flex container

        # Let's look at what's right before the first /sliding/ reference
        pre_context = html[max(0, first_sliding-500):first_sliding]
        print(f"\nContext before first /sliding/:")
        print(repr(pre_context[-300:]))

        post_context = html[last_sliding:last_sliding+500]
        print(f"\nContext after last /sliding/:")
        print(repr(post_context[:300]))

        # Strategy: find the section wrapper
        # From the HTML, the sliding section appears to be wrapped in nested divs
        # Look for the outermost wrapper by finding <section before the sliding logos
        # that isn't the Journey Through Time section

        # Find the section that wraps the sliding logos
        # The last <section open before first_sliding
        all_section_opens = [(m.start(), m.group()) for m in re.finditer(r'<section[^>]*>', html[:first_sliding])]
        if all_section_opens:
            # Get the last section open before first sliding
            wrapper_start = all_section_opens[-1][0]
            wrapper_tag = all_section_opens[-1][1]
            print(f"\nLast section open before sliding: pos {wrapper_start}, tag: {wrapper_tag[:80]}")

            # Check this isn't the Journey Through Time section
            jt_pos = html.find('A Journey Through Time')
            if wrapper_start > jt_pos:
                # Good - this section is after JT, it's likely the sliding logo wrapper

                # Find its closing </section>
                # Count section opens/closes from wrapper_start to find matching close
                depth = 0
                pos = wrapper_start
                while pos < len(html):
                    next_open = html.find('<section', pos + 1)
                    next_close = html.find('</section>', pos + 1)

                    if next_close == -1:
                        break

                    if next_open != -1 and next_open < next_close:
                        depth += 1
                        pos = next_open
                    else:
                        if depth == 0:
                            # This is our matching close
                            wrapper_end = next_close + len('</section>')
                            break
                        depth -= 1
                        pos = next_close

                region = html[wrapper_start:wrapper_end]
                sliding_count = region.count('/sliding/')
                print(f"\nRemoval region: chars {wrapper_start}-{wrapper_end} ({wrapper_end-wrapper_start} chars)")
                print(f"Contains {sliding_count} /sliding/ refs")
                print(f"Starts: {repr(region[:100])}")
                print(f"Ends: {repr(region[-100:])}")

                if sliding_count >= len(sliding_positions) // 2:  # sanity check
                    # Remove it
                    result = html[:wrapper_start] + html[wrapper_end:]

                    # Verify
                    remaining_sliding = result.count('/sliding/')
                    print(f"\nAfter removal: {len(result)} chars")
                    print(f"Remaining /sliding/ refs: {remaining_sliding}")
                    print(f"marquee-logo-new refs: {result.count('marquee-logo-new')}")

                    with open(SRC, 'w') as f:
                        f.write(result)
                    print(f"\n=== DONE! Wrote {SRC} ({len(result)} chars) ===")
                else:
                    print("ERROR: Section doesn't contain enough sliding refs. Aborting.")
            else:
                print("ERROR: Section is before Journey Through Time. Wrong section.")
        else:
            print("ERROR: No section found before sliding logos.")
    else:
        print("ERROR: Can't find new marquee section start.")
else:
    print("WARNING: Couldn't find expected pattern after sliding section.")
    # Fallback: just show context for manual analysis
    print(f"After last sliding:\n{repr(chunk_after[:500])}")
