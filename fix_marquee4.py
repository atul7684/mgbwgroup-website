#!/usr/bin/env python3
"""
Surgery 4: Remove old /sliding/ logo strip.
Strategy: Find the img tags with specific alt texts, expand outward to find
their containing div block, and remove it. Also fix logo sizes.
"""
import re, shutil

SRC = '/var/www/mgbwgroup-static/index.html'
BAK = '/var/www/mgbwgroup-static/index.html.bak4'

html = open(SRC).read()
print(f"File: {len(html)} chars")
shutil.copy2(SRC, BAK)

# Step 1: Find old logo alt texts
old_alts = ['alt="Silent Logo"', 'alt="Jg Logo"', 'alt="Garage Logo"',
            'alt="501logo Logo"', 'alt="Shukra Deepam Oil Logo"', 'alt="Shukra Logo"']

positions = []
for alt in old_alts:
    pos = html.find(alt)
    if pos > 0:
        positions.append(pos)
        print(f"  Found {alt} at {pos}")
    else:
        print(f"  NOT FOUND: {alt}")

if not positions:
    print("No old logos found — already clean?")
    exit(0)

first_pos = min(positions)
last_pos = max(positions)
print(f"\nOld logos span: {first_pos} - {last_pos}")

# Step 2: Search backward from first old logo to find the start of its container
# Look for a pattern like a div with flex/grid classes that wraps all logos
# We'll search back for the nearest section-level or major div boundary

# Find the new marquee section (background:#f8f0fc)
new_marquee_pos = html.find('background:#f8f0fc')
if new_marquee_pos < 0:
    print("ERROR: Can't find new marquee section")
    exit(1)
# Back up to find the <section that contains it
new_section_start = html.rfind('<section', 0, new_marquee_pos)
print(f"New marquee <section at: {new_section_start}")

# Step 3: Find "Growth Across Sectors" - last JT timeline entry
growth_pos = html.find('Growth Across Sectors')
if growth_pos < 0:
    print("ERROR: Can't find 'Growth Across Sectors'")
    exit(1)
print(f"'Growth Across Sectors' at: {growth_pos}")

# Step 4: The old logo block is between growth_pos and new_section_start
# Let's just look at what's in between and find reasonable cut points
between = html[growth_pos:new_section_start]
print(f"\nContent between Growth and new marquee: {len(between)} chars")

# Find the first old logo position relative to growth_pos
# The old logos are inside some nested divs between the JT section end and new marquee
# Strategy: cut from just before first old logo's outermost container to new marquee start

# Search backward from first_pos to find a good cut start
# Look for a <div that starts a logo container section
# Scan back to find something like a section break or major container
search_back = html[growth_pos:first_pos]
print(f"\nSearching back from first old logo ({first_pos}) to Growth ({growth_pos})...")

# Find all </section> and <section in the gap
for m in re.finditer(r'</section>|<section', search_back):
    print(f"  Tag at offset +{m.start()}: {m.group()}")

# Find </div> tags just before first old logo to find container boundary
# Let's try: look for the section/div boundary closest before the first logo
# and use that + the new marquee start as removal bounds

# Alternative simpler approach:
# Find the chunk from after the last </p> or </div> before old logos
# to just before new marquee <section

# Let's find what's right before the first img with old alt text
# Back up to find the img tag start
img_start = html.rfind('<img', 0, first_pos)
print(f"\nFirst old <img at: {img_start}")

# Now find the outermost container div for these logos
# Keep going back looking for divs that contain all the old logos
# Simple approach: find the nearest <div before img_start that ALSO
# has a matching </div> after last_pos

# Even simpler: just search for a recognizable class pattern before first_pos
# Look for "flex items-center justify-center gap" near the old logos
flex_pattern = html.rfind('flex items-center justify-center gap', 0, first_pos)
if flex_pattern > 0:
    # Back up to the <div that contains this class
    div_start = html.rfind('<div', 0, flex_pattern)
    print(f"Found flex container <div at: {div_start}")
else:
    print("No flex container found, using img_start area")
    div_start = img_start

# Now let's be more precise. Let's look at a window around the old logos
window_start = max(0, first_pos - 500)
window_end = min(len(html), last_pos + 500)
print(f"\n=== CONTEXT AROUND OLD LOGOS (chars {window_start}-{window_end}) ===")
print(html[window_start:first_pos][-300:])
print("--- FIRST OLD LOGO HERE ---")
print(html[last_pos:last_pos+200])
print("=== END CONTEXT ===")

# Step 5: Now let's find the removal boundaries more carefully
# Look for a clear structural boundary between JT content and old logos
# and between old logos and new marquee

# Search for the LAST </section> before the old logos and after Growth
# Actually, let's find ALL section boundaries in the gap
gap_html = html[growth_pos:new_section_start]
print(f"\n=== SECTION TAGS IN GAP ({growth_pos} to {new_section_start}) ===")
for m in re.finditer(r'</?section[^>]*>', gap_html):
    abs_pos = growth_pos + m.start()
    print(f"  char {abs_pos}: {m.group()[:80]}")

# Step 6: Let's try a different cut strategy
# Find everything between the last </section> before old logos and the new marquee <section
# If no </section> found, find the last </div> cluster before old logos

# Look for </section> between growth and first old logo
last_section_close = -1
for m in re.finditer(r'</section>', html[growth_pos:first_pos]):
    last_section_close = growth_pos + m.start()

if last_section_close > 0:
    cut_start = last_section_close + len('</section>')
    print(f"\nCut start (after </section>): {cut_start}")
else:
    # No </section> between growth and logos - look for a div boundary
    # Find the region we need to cut by looking at what's between growth area and new marquee
    # Just cut from 200 chars before first old img to new marquee start
    cut_start = html.rfind('\n', 0, div_start)
    if cut_start < 0:
        cut_start = div_start
    print(f"\nCut start (before flex div): {cut_start}")

cut_end = new_section_start
print(f"Cut end (new marquee <section): {cut_end}")
print(f"Removing {cut_end - cut_start} chars")

# Show what we're removing (first/last 200 chars)
to_remove = html[cut_start:cut_end]
print(f"\n=== REMOVING (first 300 chars) ===")
print(to_remove[:300])
print(f"\n=== REMOVING (last 300 chars) ===")
print(to_remove[-300:])

# SAFETY: verify old logos ARE in the removal zone and new marquee is NOT
old_in_zone = sum(1 for alt in old_alts if alt in to_remove)
new_marquee_in_zone = 'marquee-logo-new' in to_remove
print(f"\nSafety: {old_in_zone}/{len(old_alts)} old logos in removal zone")
print(f"Safety: new marquee in zone = {new_marquee_in_zone}")

if old_in_zone == 0:
    print("ERROR: No old logos in removal zone! Aborting.")
    exit(1)
if new_marquee_in_zone:
    print("ERROR: New marquee would be removed! Aborting.")
    exit(1)

# Step 7: Remove the old logo block
html = html[:cut_start] + '\n' + html[cut_end:]
print(f"\nAfter removal: {len(html)} chars")

# Step 8: Verify no old logo alt texts remain
for alt in old_alts:
    if alt in html:
        print(f"WARNING: {alt} still in file!")

# Step 9: Fix logo heights - change 80px to 120px in marquee
old_height = '.marquee-logo-new{height:80px'
new_height = '.marquee-logo-new{height:120px'
# Try with spaces too
patterns = [
    ('height:80px', 'height:120px'),  # in .marquee-logo-new CSS
    ('height: 80px', 'height: 120px'),
]

# Find the marquee CSS block and only change height there
marquee_css_start = html.find('.marquee-logo-new')
if marquee_css_start > 0:
    marquee_css_end = html.find('}', marquee_css_start)
    css_block = html[marquee_css_start:marquee_css_end+1]
    print(f"\nMarquee CSS: {css_block}")
    new_css = css_block.replace('height:80px', 'height:120px').replace('height: 80px', 'height: 120px')
    if new_css != css_block:
        html = html[:marquee_css_start] + new_css + html[marquee_css_end+1:]
        print(f"Updated CSS: {new_css}")
    else:
        print("No height change needed in CSS")

# Step 10: Add style="height:80px" to Modern Kitchens and Shukra Deepam logos
for logo_name in ['modern_kitchens_logo.png', 'shukra_deepam_logo.png']:
    # Find all img tags with this src
    pattern = f'src="/marquee_logos/{logo_name}"'
    idx = 0
    count = 0
    while True:
        pos = html.find(pattern, idx)
        if pos < 0:
            break
        # Check if already has style="height:80px"
        img_start = html.rfind('<img', 0, pos)
        img_end = html.find('>', pos)
        img_tag = html[img_start:img_end+1]
        if 'style="height:80px"' not in img_tag and "style='height:80px'" not in img_tag:
            # Add style attribute
            html = html[:img_start] + '<img style="height:80px" ' + html[img_start+4:]
            count += 1
        idx = pos + len(pattern)
    print(f"Added height:80px to {count} {logo_name} tags")

# Write result
open(SRC, 'w').write(html)
print(f"\nFinal file: {len(html)} chars")
print("DONE!")
