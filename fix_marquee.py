#!/usr/bin/env python3
"""
Surgery script: Remove old logo strips, insert new scrolling marquee.
Runs on VPS at /var/www/mgbwgroup-static/
"""
import re, shutil, os

SRC = '/var/www/mgbwgroup-static/index.html'
BAK = '/var/www/mgbwgroup-static/index.html.bak_marquee'

# New marquee HTML
NEW_MARQUEE = '''<section class="w-full py-10" style="background:#f8f0fc;overflow:hidden;">
<style>
@keyframes marqueeScroll { 0% { transform: translateX(0); } 100% { transform: translateX(-50%); } }
.marquee-container { overflow: hidden; width: 100%; position: relative; }
.marquee-track { display: flex; align-items: center; animation: marqueeScroll 25s linear infinite; width: max-content; }
.marquee-track:hover { animation-play-state: paused; }
.marquee-logo-new { height: 80px; width: auto; object-fit: contain; flex-shrink: 0; margin: 0 40px; }
</style>
<div class="marquee-container"><div class="marquee-track">
<img src="/marquee_logos/mgbw_main_logo.png" class="marquee-logo-new" alt="MGBW Main Logo">
<img src="/marquee_logos/shukra_beedies_logo.png" class="marquee-logo-new" alt="Shukra Beedies Logo">
<img src="/marquee_logos/silent_shores_logo.png" class="marquee-logo-new" alt="Silent Shores Logo">
<img src="/marquee_logos/jg_agarbathies_logo.png" class="marquee-logo-new" alt="J&amp;G Agarbathies Logo">
<img src="/marquee_logos/mgbw_garage_logo.png" class="marquee-logo-new" alt="MGBW Garage Logo">
<img src="/marquee_logos/modern_kitchens_logo.png" class="marquee-logo-new" alt="Modern Kitchens Logo">
<img src="/marquee_logos/501_matches_logo.png" class="marquee-logo-new" alt="501 Matches Logo">
<img src="/marquee_logos/shukra_deepam_logo.png" class="marquee-logo-new" alt="Shukra Deepam Logo">
<img src="/marquee_logos/mgbw_main_logo.png" class="marquee-logo-new" alt="MGBW Main Logo">
<img src="/marquee_logos/shukra_beedies_logo.png" class="marquee-logo-new" alt="Shukra Beedies Logo">
<img src="/marquee_logos/silent_shores_logo.png" class="marquee-logo-new" alt="Silent Shores Logo">
<img src="/marquee_logos/jg_agarbathies_logo.png" class="marquee-logo-new" alt="J&amp;G Agarbathies Logo">
<img src="/marquee_logos/mgbw_garage_logo.png" class="marquee-logo-new" alt="MGBW Garage Logo">
<img src="/marquee_logos/modern_kitchens_logo.png" class="marquee-logo-new" alt="Modern Kitchens Logo">
<img src="/marquee_logos/501_matches_logo.png" class="marquee-logo-new" alt="501 Matches Logo">
<img src="/marquee_logos/shukra_deepam_logo.png" class="marquee-logo-new" alt="Shukra Deepam Logo">
</div></div>
</section>'''

print("=== Marquee Surgery Script ===")

# 1. Read file
html = open(SRC).read()
orig_len = len(html)
print(f"Original file: {orig_len} chars")

# 2. Backup
shutil.copy2(SRC, BAK)
print(f"Backup saved: {BAK}")

# 3. Find all sections containing marquee-logo class
# Strategy: find the outermost <section> or <div> wrappers around marquee-logo images
# Look for patterns of <section...>...<img...marquee-logo...>...</section>

# First, let's find all marquee-logo positions
ml_positions = []
start = 0
while True:
    idx = html.find('marquee-logo', start)
    if idx == -1:
        break
    ml_positions.append(idx)
    start = idx + 1

print(f"Found {len(ml_positions)} marquee-logo occurrences at positions: {ml_positions[:3]}...{ml_positions[-3:]}")

if not ml_positions:
    print("ERROR: No marquee-logo found! Aborting.")
    exit(1)

# Group into clusters (sections) - positions close together are same section
clusters = []
current_cluster = [ml_positions[0]]
for pos in ml_positions[1:]:
    if pos - current_cluster[-1] < 500:  # within 500 chars = same cluster
        current_cluster.append(pos)
    else:
        clusters.append(current_cluster)
        current_cluster = [pos]
clusters.append(current_cluster)

print(f"Found {len(clusters)} logo strip cluster(s):")
for i, c in enumerate(clusters):
    print(f"  Cluster {i+1}: {len(c)} logos, chars {c[0]}-{c[-1]}")

# 4. For each cluster, find the wrapping section/div
# Walk backward from first marquee-logo in cluster to find <section or <div with class containing relevant wrapper
# Walk forward from last marquee-logo to find closing </section> or </div>

regions_to_remove = []

for ci, cluster in enumerate(clusters):
    first_pos = cluster[0]
    last_pos = cluster[-1]

    # Walk backward to find opening tag of wrapper
    # Look for <section or <div that wraps this whole block
    # Search backward for section tags
    search_start = max(0, first_pos - 2000)
    chunk_before = html[search_start:first_pos]

    # Find the last <section before the marquee-logo block
    # Could also be a <div with specific class
    # Try to find section first
    section_opens = []
    for m in re.finditer(r'<section[^>]*>', chunk_before):
        section_opens.append(search_start + m.start())

    div_opens = []
    for m in re.finditer(r'<div[^>]*>', chunk_before):
        div_opens.append(search_start + m.start())

    # Also check for style blocks that might be part of the logo strip
    style_opens = []
    for m in re.finditer(r'<style[^>]*>', chunk_before):
        style_opens.append(search_start + m.start())

    # Find closing after last marquee-logo
    search_end = min(len(html), last_pos + 2000)
    chunk_after = html[last_pos:search_end]

    section_closes = []
    for m in re.finditer(r'</section>', chunk_after):
        section_closes.append(last_pos + m.start() + len('</section>'))

    div_closes = []
    for m in re.finditer(r'</div>', chunk_after):
        div_closes.append(last_pos + m.start() + len('</div>'))

    # Strategy: take the nearest <section before and </section> after
    # If no section, use div
    if section_opens and section_closes:
        region_start = section_opens[-1]  # closest section open before
        region_end = section_closes[0]    # first section close after
    elif div_opens and div_closes:
        region_start = div_opens[-1]
        region_end = div_closes[0]
    else:
        # Fallback: just remove the img tags area with some padding
        region_start = first_pos - 100
        region_end = last_pos + 200

    # Verify this region actually contains all the marquee-logo refs
    region_text = html[region_start:region_end]
    ml_count = region_text.count('marquee-logo')
    print(f"  Cluster {ci+1} removal region: chars {region_start}-{region_end} ({region_end-region_start} chars, contains {ml_count} marquee-logo refs)")

    # Show first 100 chars of region for verification
    print(f"  Starts with: {repr(region_text[:100])}")
    print(f"  Ends with: {repr(region_text[-100:])}")

    regions_to_remove.append((region_start, region_end))

# 5. Find where to insert new marquee - after "A Journey Through Time" section
jt_pos = html.find('A Journey Through Time')
if jt_pos == -1:
    print("ERROR: 'A Journey Through Time' not found! Aborting.")
    exit(1)

print(f"\n'A Journey Through Time' found at char {jt_pos}")

# Find the </section> that closes the Journey Through Time section
# The JT section should end before the logo strips begin
# Look for </section> between JT position and first logo strip
first_strip_start = regions_to_remove[0][0] if regions_to_remove else len(html)
jt_to_strip = html[jt_pos:first_strip_start]

# Find all </section> closings in this range
section_ends = []
for m in re.finditer(r'</section>', jt_to_strip):
    section_ends.append(jt_pos + m.start() + len('</section>'))

if section_ends:
    insert_pos = section_ends[-1]  # last </section> before the logo strips
    print(f"Insert position: char {insert_pos} (last </section> between JT and logo strips)")
else:
    # If no section end found, insert just before the first logo strip
    insert_pos = first_strip_start
    print(f"Insert position: char {insert_pos} (just before first logo strip)")

# 6. Perform surgery - work from end to start to preserve positions
# Sort regions by start position, reverse
regions_to_remove.sort(key=lambda r: r[0], reverse=True)

result = html

# First remove all old logo strip regions (from end to start)
for start, end in regions_to_remove:
    # Adjust insert_pos if removal is before it
    if start < insert_pos:
        # This removal shifts insert_pos
        removed_len = end - start
        if end <= insert_pos:
            insert_pos -= removed_len
        elif start < insert_pos:
            insert_pos = start
    result = result[:start] + result[end:]

print(f"\nAfter removing {len(regions_to_remove)} strip(s): {len(result)} chars (removed {orig_len - len(result)} chars)")

# Now insert new marquee at adjusted position
result = result[:insert_pos] + NEW_MARQUEE + result[insert_pos:]

print(f"After inserting new marquee: {len(result)} chars")

# 7. Verify
assert 'marquee-logo-new' in result, "New marquee not found in result!"
old_ml_count = result.count('marquee-logo"')  # old class (without -new)
new_ml_count = result.count('marquee-logo-new')
print(f"\nVerification:")
print(f"  Old 'marquee-logo' class refs: {old_ml_count}")
print(f"  New 'marquee-logo-new' class refs: {new_ml_count}")
print(f"  'marquee_logos/' image paths: {result.count('marquee_logos/')}")
print(f"  'A Journey Through Time' present: {'A Journey Through Time' in result}")

if old_ml_count > 0:
    print(f"  WARNING: {old_ml_count} old marquee-logo refs remain!")

# 8. Write result
with open(SRC, 'w') as f:
    f.write(result)

print(f"\n=== DONE! File written: {SRC} ({len(result)} chars) ===")
print(f"Backup at: {BAK}")
