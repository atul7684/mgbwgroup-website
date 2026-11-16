#!/usr/bin/env python3
"""Fix J&G agarbatti image paths in HTML files.

The HTML references paths like:
  /ourbusiness/j&dagarbatti/fragrances/champa.png
  /ourbusiness/j&amp;dagarbatti/fragrances/champa.png

We serve files from:
  /ourbusiness/jgagarbatti/fragrances/champa.png

This script rewrites all j&d/j&amp;d variations to jgagarbatti.
Also handles the 5 page images (help, market, partner, product, whatmakes).
"""

import os
import re
import glob
import shutil

ROOT = '/var/www/mgbwgroup-static'

# Find all HTML files
html_files = glob.glob(os.path.join(ROOT, '*.html')) + \
             glob.glob(os.path.join(ROOT, '**/*.html'), recursive=True)

# Patterns to replace - all variations of the J&G path
# The key insight: HTML uses j&dagarbatti or j&amp;dagarbatti
# We serve from jgagarbatti

replacements = {}
count = 0

for html_file in html_files:
    with open(html_file, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    original = content

    # Replace all variations of j&dagarbatti and j&amp;dagarbatti with jgagarbatti
    # Pattern 1: /ourbusiness/j&dagarbatti/ -> /ourbusiness/jgagarbatti/
    content = content.replace('/ourbusiness/j&dagarbatti/', '/ourbusiness/jgagarbatti/')
    # Pattern 2: /ourbusiness/j&amp;dagarbatti/ -> /ourbusiness/jgagarbatti/
    content = content.replace('/ourbusiness/j&amp;dagarbatti/', '/ourbusiness/jgagarbatti/')
    # Pattern 3: ourbusiness/j&dagarbatti/ (without leading slash)
    content = content.replace('ourbusiness/j&dagarbatti/', 'ourbusiness/jgagarbatti/')
    content = content.replace('ourbusiness/j&amp;dagarbatti/', 'ourbusiness/jgagarbatti/')

    if content != original:
        # Backup
        backup = html_file + '.bak_jgfix'
        if not os.path.exists(backup):
            shutil.copy2(html_file, backup)

        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)

        # Count changes
        changes = 0
        for line_num, (old_line, new_line) in enumerate(
            zip(original.split('\n'), content.split('\n')), 1):
            if old_line != new_line:
                changes += 1

        print(f"Fixed {html_file}: {changes} lines changed")
        count += 1

print(f"\nTotal: {count} files modified")

# Now check what J&G paths remain that might still be broken
print("\n=== Remaining J&G references ===")
for html_file in html_files:
    with open(html_file, 'r', encoding='utf-8', errors='replace') as f:
        for line_num, line in enumerate(f, 1):
            if 'jgagarbatti' in line.lower() or 'j&g' in line.lower() or 'j&dagarbatti' in line.lower():
                # Extract src/href attributes
                for match in re.finditer(r'(?:src|href)=["\']([^"\']*(?:jgagarbatti|j&g|j&dagarbatti|j&amp;dagarbatti)[^"\']*)["\']', line, re.IGNORECASE):
                    path = match.group(1)
                    # Check if file exists
                    full_path = os.path.join(ROOT, path.lstrip('/'))
                    exists = os.path.exists(full_path)
                    status = "OK" if exists else "MISSING"
                    print(f"  [{status}] {os.path.basename(html_file)}:{line_num} -> {path}")
