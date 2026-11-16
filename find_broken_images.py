#!/usr/bin/env python3
"""Find all broken image paths across all HTML files and map to actual files."""
import re, glob, os

root = '/var/www/mgbwgroup-static'
html_files = glob.glob(root + '/*.html') + glob.glob(root + '/businesses/*.html')

# Collect all broken src paths
all_broken = {}  # path -> list of files using it
for f in html_files:
    with open(f) as fh:
        html = fh.read()
    for m in re.finditer(r'src=[\'"](/[^\s\'"]+\.(?:WEBP|webp|png|jpg|jpeg|gif|svg|mp4|ico))', html, re.I):
        path = m.group(1)
        full = root + path
        if not os.path.exists(full):
            if path not in all_broken:
                all_broken[path] = []
            all_broken[path].append(os.path.basename(f))

print(f"=== {len(all_broken)} BROKEN IMAGE PATHS ===\n")
for p in sorted(all_broken.keys()):
    print(f"  {p}")
    print(f"    used in: {', '.join(all_broken[p])}")

# Now find all actual image files on disk
print(f"\n=== ACTUAL IMAGE FILES ===\n")
actual_files = {}
for dirpath, dirnames, filenames in os.walk(root):
    # Skip .git and node_modules
    dirnames[:] = [d for d in dirnames if d not in ('.git', 'node_modules', '.next')]
    for fn in filenames:
        if fn.lower().endswith(('.webp', '.png', '.jpg', '.jpeg', '.gif', '.svg', '.mp4', '.ico')):
            rel = os.path.join(dirpath, fn)[len(root):]
            actual_files[fn.lower()] = rel

# Try to map broken paths to actual files
print(f"\n=== MAPPING SUGGESTIONS ===\n")
for broken_path in sorted(all_broken.keys()):
    basename = os.path.basename(broken_path).lower()
    # Try exact basename match
    if basename in actual_files:
        print(f"  {broken_path}")
        print(f"    -> {actual_files[basename]}")
    else:
        # Try partial match
        matches = [v for k, v in actual_files.items() if basename.replace('.webp','').replace('.png','').replace('.jpg','') in k]
        if matches:
            print(f"  {broken_path}")
            print(f"    ~> {matches[0]} (partial)")
        else:
            print(f"  {broken_path}")
            print(f"    -> NO MATCH FOUND")
