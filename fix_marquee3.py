#!/usr/bin/env python3
"""
Surgery 3: Remove old /sliding/ logo strip by finding the specific img tags
with alt text like "Silent Logo", "Jg Logo", "Garage Logo" etc.
Then also increase logo height from 80px to 120px for the new marquee,
but keep Modern Kitchens and Shukra Deepam at 80px.
"""
import re, shutil

SRC = '/var/www/mgbwgroup-static/index.html'
BAK = '/var/www/mgbwgroup-static/index.html.bak3'

html = open(SRC).read()
print(f"File: {len(html)} chars")
shutil.copy2(SRC, BAK)

# Step 1: Find the old sliding logo block
# These logos have alt text like "Silent Logo", "Jg Logo", "Garage Logo", "501logo Logo", "Shukra Deepam Oil Logo"
# and src paths like /sliding/shukra.WEBP, /sliding/silent.WEBP etc.
# They are wrapped in flex div containers

# Find specific alt tags that belong to old logos (NOT in our new marquee which uses different alt texts)
old_logo_alts = ['alt="Silent Logo"', 'alt="Jg Logo"', 'alt="Garage Logo"', 'alt="501logo Logo"', 'alt="Shukra Deepam Oil Logo"', 'alt="Shukra Logo"']

old_logo_positions = []
for alt in old_logo_alts:
    pos = html.find(alt)
    if pos > 0:
        old_logo_positions.append(pos)
        print(f"  {alt} at char {pos}")

if not old_logo_positions:
    print("No old logo alt tags found. Maybe already removed.")
else:
    first_old = min(old_logo_positions)
    last_old = max(old_logo_positions)
    print(f"\nOld logos span: chars {first_old} - {last_old}")

    # Find the wrapper: look for the nearest <section or major wrapper div
    # that encompasses all these logos
    # Look backward from first_old for <section
    search_start = max(0, first_old - 2000)
    chunk = html[search_start:first_old]

    # Find section opens in this chunk
    sections = [(search_start + m.start()) for m in re.finditer(r'<section[^>]*>', chunk)]
    # Find div class="overflow-hidden" or similar wrapper
    overflow_divs = [(search_start + m.start()) for m in re.finditer(r'<div[^>]*overflow[^>]*>', chunk)]

    print(f"Section opens before logos: {sections}")
    print(f"Overflow div opens: {overflow_divs}")

    # Look forward from last_old for closing
    search_end = min(len(html), last_old + 1000)
    after = html[last_old:search_end]

    # Find where new marquee starts (our section with #f8f0fc)
    new_marquee_pos = html.find('background:#f8f0fc', last_old)
    print(f"New marquee section at: {new_marquee_pos}")

    if new_marquee_pos > 0:
        # Find the <section that starts our new marquee
        # Walk backward from new_marquee_pos to find <section
        pre_new = html[max(0, new_marquee_pos - 100):new_marquee_pos]
        sec_match = pre_new.rfind('<section')
        if sec_match >= 0:
            new_section_start = max(0, new_marquee_pos - 100) + sec_match
            print(f"New marquee <section starts at: {new_section_start}")

            # The old logo section is everything between end of JT section and start of new marquee
            # Let's find what's between the last timeline entry and new marquee
            # Find "Growth Across Sectors" (last timeline entry)
            growth_pos = html.find('Growth Across Sectors')
            print(f"'Growth Across Sectors' at: {growth_pos}")

            if growth_pos > 0:
                # Find the </section> that closes the Journey Through Time section
                # It's after "Growth Across Sectors" and before the old logo block
                jt_end_region = html[growth_pos:first_old]
                # Find last </section> in this region
                sec_closes = [growth_pos + m.start() + len('</section>') for m in re.finditer(r'</section>', jt_end_region)]

                if sec_closes:
                    jt_section_end = sec_closes[-1]
                    print(f"JT section ends at: {jt_section_end}")

                    # Everything between JT section end and new marquee section start is the old logo block
                    old_block = html[jt_section_end:new_section_start]
                    old_sliding_count = old_block.count('/sliding/')
                    old_alt_count = sum(1 for alt in old_logo_alts if alt in old_block)

                    print(f"\nOld block to remove: chars {jt_section_end} - {new_section_start} ({new_section_start - jt_section_end} chars)")
                    print(f"Contains {old_sliding_count} /sliding/ refs, {old_alt_count} old logo alt tags")
                    print(f"Starts: {repr(old_block[:150])}")
                    print(f"Ends: {repr(old_block[-150:])}")

                    # Remove the old block
                    result = html[:jt_section_end] + html[new_section_start:]

                    remaining_old_alts = sum(1 for alt in old_logo_alts if alt in result)
                    print(f"\nAfter removal: {len(result)} chars")
                    print(f"Remaining old logo alts: {remaining_old_alts}")
                    print(f"marquee-logo-new refs: {result.count('marquee-logo-new')}")

                    # Step 2: Increase logo sizes in new marquee
                    # Change height from 80px to 120px for all logos
                    # Then set Modern Kitchens and Shukra Deepam back to 80px via inline style
                    result = result.replace(
                        '.marquee-logo-new { height: 80px;',
                        '.marquee-logo-new { height: 120px;'
                    )

                    # Add specific size overrides for Modern Kitchens and Shukra Deepam
                    # These two should stay at 80px per user request
                    result = result.replace(
                        'alt="Modern Kitchens Logo">',
                        'alt="Modern Kitchens Logo" style="height:80px">'
                    )
                    result = result.replace(
                        'alt="Shukra Deepam Logo">',
                        'alt="Shukra Deepam Logo" style="height:80px">'
                    )

                    print(f"Logo heights updated: 120px default, 80px for Modern Kitchens and Shukra Deepam")

                    with open(SRC, 'w') as f:
                        f.write(result)
                    print(f"\n=== DONE! Wrote {SRC} ({len(result)} chars) ===")
                else:
                    print("ERROR: No </section> found between Growth and old logos")
            else:
                print("ERROR: 'Growth Across Sectors' not found")
    else:
        print("ERROR: New marquee section not found")
