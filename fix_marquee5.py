#!/usr/bin/env python3
"""
Surgery 5: Precisely remove old /sliding/ logo strip.
Strategy: Find the specific container div with background-color:#ffffff
that contains the old logo images, remove just that div.
Also fix logo sizes in new marquee.
"""
import shutil

SRC = '/var/www/mgbwgroup-static/index.html'
BAK = '/var/www/mgbwgroup-static/index.html.bak5'

html = open(SRC).read()
print(f"File: {len(html)} chars")
shutil.copy2(SRC, BAK)

# Step 1: Find the old logo container
# It starts with: <div class="py-8  relative overflow-hidden" style="background-color:#ffffff">
# and contains all the old /sliding/ logos
# We need to find THIS specific div (not any other bg-white div)

# Find "Mgbwworks Logo" - unique to old sliding section
marker = 'alt="Mgbwworks Logo"'
marker_pos = html.find(marker)
if marker_pos < 0:
    # Try alternate
    marker = 'alt="Silent Logo"'
    marker_pos = html.find(marker)
if marker_pos < 0:
    print("No old logos found — already clean")
    exit(0)
print(f"Found old logo marker at char {marker_pos}")

# Step 2: Search backward from marker to find the container div
# Look for the py-8 relative overflow-hidden div with background-color:#ffffff
search_back = html[max(0, marker_pos-2000):marker_pos]

# Find "background-color:#ffffff" in the region before old logos
bg_pos = search_back.rfind('background-color:#ffffff')
if bg_pos < 0:
    bg_pos = search_back.rfind('background-color: #ffffff')
if bg_pos < 0:
    print("ERROR: Can't find background-color:#ffffff container")
    # Try finding py-8 overflow-hidden
    bg_pos = search_back.rfind('py-8')
    if bg_pos < 0:
        print("ERROR: Can't find py-8 container either")
        exit(1)

# Convert to absolute position
abs_bg_pos = max(0, marker_pos-2000) + bg_pos
print(f"Found container style at char {abs_bg_pos}")

# Find the <div that contains this style
div_start = html.rfind('<div', 0, abs_bg_pos + 10)
print(f"Container <div starts at char {div_start}")

# Step 3: Now find the matching closing </div> for this container
# Count div nesting from div_start
depth = 0
i = div_start
container_end = -1
while i < len(html):
    if html[i:i+4] == '<div':
        depth += 1
        i += 4
    elif html[i:i+6] == '</div>':
        depth -= 1
        if depth == 0:
            container_end = i + 6
            break
        i += 6
    else:
        i += 1

if container_end < 0:
    print("ERROR: Couldn't find matching </div>")
    exit(1)

print(f"Container ends at char {container_end}")
print(f"Container size: {container_end - div_start} chars")

# Step 4: Verify this container has old logos and NOT new marquee
container = html[div_start:container_end]
has_old = 'alt="Silent Logo"' in container or '/sliding/' in container
has_new = 'marquee-logo-new' in container
print(f"Has old logos: {has_old}")
print(f"Has new marquee: {has_new}")

if not has_old:
    print("ERROR: Container doesn't have old logos!")
    exit(1)
if has_new:
    print("ERROR: Container includes new marquee!")
    exit(1)

# Show what we're removing (first/last bits)
print(f"\n=== REMOVING (first 200 chars) ===")
print(container[:200])
print(f"\n=== REMOVING (last 200 chars) ===")
print(container[-200:])

# Step 5: Remove the container
html = html[:div_start] + html[container_end:]
print(f"\nAfter removal: {len(html)} chars")

# Verify old logos gone
for alt in ['alt="Silent Logo"', 'alt="Jg Logo"', 'alt="Garage Logo"', 'alt="Shukra Logo"']:
    if alt in html:
        print(f"WARNING: {alt} still present!")
    else:
        print(f"OK: {alt} removed")

# Step 6: Fix logo heights in new marquee
marquee_css_start = html.find('.marquee-logo-new')
if marquee_css_start > 0:
    marquee_css_end = html.find('}', marquee_css_start)
    css_block = html[marquee_css_start:marquee_css_end+1]
    print(f"\nMarquee CSS: {css_block}")
    new_css = css_block.replace('height:80px', 'height:120px').replace('height: 80px', 'height: 120px')
    if new_css != css_block:
        html = html[:marquee_css_start] + new_css + html[marquee_css_end+1:]
        print(f"Updated CSS: {new_css}")

# Step 7: Add height:80px to Modern Kitchens and Shukra Deepam
for logo_name in ['modern_kitchens_logo.png', 'shukra_deepam_logo.png']:
    pattern = f'src="/marquee_logos/{logo_name}"'
    idx = 0
    count = 0
    while True:
        pos = html.find(pattern, idx)
        if pos < 0:
            break
        img_start = html.rfind('<img', 0, pos)
        img_tag = html[img_start:pos+len(pattern)+5]
        if 'style="height:80px"' not in img_tag:
            html = html[:img_start] + '<img style="height:80px" ' + html[img_start+4:]
            count += 1
        idx = pos + len(pattern) + 20
    print(f"Added height:80px to {count} {logo_name} tags")

# Write
open(SRC, 'w').write(html)
print(f"\nFinal: {len(html)} chars")
print("DONE!")
