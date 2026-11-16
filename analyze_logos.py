#!/usr/bin/env python3
"""Analyze the HTML structure around old logo images"""
html = open('/var/www/mgbwgroup-static/index.html').read()

# Find Silent Logo position
pos = html.find('alt="Silent Logo"')
print(f"Silent Logo at char {pos}")

# Show 1500 chars before it
start = max(0, pos - 1500)
print(f"\n=== 1500 chars BEFORE Silent Logo (chars {start}-{pos}) ===")
print(html[start:pos])

# Find last old logo
last_pos = html.find('alt="Shukra Logo"')
print(f"\nShukra Logo at char {last_pos}")

# Show 500 chars after last logo
end = min(len(html), last_pos + 500)
print(f"\n=== 500 chars AFTER Shukra Logo ===")
print(html[last_pos:end])

# Find new marquee
new_m = html.find('background:#f8f0fc')
new_s = html.rfind('<section', 0, new_m)
print(f"\nNew marquee <section at char {new_s}")
print(f"Chars between last old logo and new marquee: {new_s - last_pos}")
