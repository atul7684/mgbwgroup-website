#!/usr/bin/env python3
"""
Fix broken image/video paths in all HTML files.
Strategy:
1. Build a map of all actual image files on disk (relative to web root)
2. Extract all image src references from HTML files
3. For each broken path, try to find matching actual file using naming patterns
4. Do search-and-replace in HTML files
5. For truly missing files (no match on disk), create symlinks or report
"""

import os
import re
import glob
from pathlib import Path

ROOT = '/var/www/mgbwgroup-static'

# Step 1: Build inventory of all actual image/video files
def get_all_media_files():
    """Get all image/video files relative to web root"""
    extensions = {'.png', '.jpg', '.jpeg', '.webp', '.svg', '.gif', '.mp4', '.ico'}
    files = {}
    for dirpath, dirnames, filenames in os.walk(ROOT):
        for f in filenames:
            full = os.path.join(dirpath, f)
            rel = full[len(ROOT):]  # starts with /
            ext = os.path.splitext(f)[1].lower()
            if ext in extensions:
                basename = os.path.basename(f).lower()
                files[rel] = full
                # Also index by lowercase basename for fuzzy matching
                if basename not in files:
                    files['_basename_' + basename] = rel
    return files

# Step 2: Extract broken image paths from HTML
def get_broken_paths():
    """Find all image src paths in HTML that don't resolve to actual files"""
    html_files = glob.glob(os.path.join(ROOT, '*.html')) + \
                 glob.glob(os.path.join(ROOT, 'businesses', '*.html'))

    broken = {}  # path -> list of html files using it
    pattern = re.compile(r'(?:src|poster)=["\'](/[^"\'?#]+\.(?:png|jpg|jpeg|webp|svg|gif|mp4|ico|WEBP|PNG|JPG))', re.IGNORECASE)

    for html_file in html_files:
        with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        matches = pattern.findall(content)
        rel_html = os.path.relpath(html_file, ROOT)

        for path in matches:
            full_path = os.path.join(ROOT, path.lstrip('/'))
            if not os.path.exists(full_path):
                if path not in broken:
                    broken[path] = []
                if rel_html not in broken[path]:
                    broken[path].append(rel_html)

    return broken

# Step 3: Build path mappings
def build_mappings(broken_paths, actual_files):
    """Try to map broken paths to actual files"""
    mappings = {}  # broken_path -> actual_path
    missing = {}   # broken_path -> html files (truly missing, no match)

    for broken_path, html_files in broken_paths.items():
        actual = find_actual_path(broken_path, actual_files)
        if actual:
            mappings[broken_path] = actual
        else:
            missing[broken_path] = html_files

    return mappings, missing

def find_actual_path(broken_path, actual_files):
    """Try various strategies to find the actual file for a broken path"""

    # Strategy 1: Direct match (maybe case difference)
    if broken_path in actual_files:
        return broken_path

    # Strategy 2: Check if path without /images/ prefix exists with it
    # e.g. /about/X.png -> /images/about/X.png
    if not broken_path.startswith('/images/'):
        with_images = '/images' + broken_path
        if with_images in actual_files:
            return with_images

    # Strategy 3: Next.js dynamic route pattern
    # /ourbusiness/ganeshbeedi/501/1st.WEBP -> /business/ganeshbeedi/ourbusiness_ganeshbeedi_501_1st.WEBP
    # /ourbusiness/ganeshbeedi/scalling/ganeshbeediii.WEBP -> /business/ganeshbeedi/ourbusiness_ganeshbeedi_scalling_ganeshbeediii.WEBP
    m = re.match(r'^/ourbusiness/([^/]+)/(.+)$', broken_path)
    if m:
        business_name = m.group(1)
        rest = m.group(2)
        # Map business names
        biz_map = {
            'ganeshbeedi': 'ganeshbeedi',
            'sukrabeedi': 'shukrabeedi',
            'j&dagarbatti': 'jgagarbatti',
            'j&amp;dagarbatti': 'jgagarbatti',
        }
        mapped_biz = biz_map.get(business_name, business_name)

        # Build flattened name: ourbusiness_BIZNAME_rest_with_underscores
        rest_parts = rest.replace('/', '_')
        # Try: /business/MAPPED_BIZ/ourbusiness_BIZNAME_REST
        prefix_name = f'ourbusiness_{business_name.replace("&", "").replace("amp;", "")}'

        # For ganeshbeedi
        if business_name == 'ganeshbeedi':
            candidate = f'/business/ganeshbeedi/ourbusiness_ganeshbeedi_{rest_parts}'
            if candidate in actual_files:
                return candidate

        # For sukrabeedi
        if business_name == 'sukrabeedi':
            candidate = f'/business/shukrabeedi/ourbusiness_sukrabeedi_{rest_parts}'
            if candidate in actual_files:
                return candidate
            # Try with different spelling
            rest_mapped = rest_parts.replace('background', 'background')
            candidate2 = f'/business/shukrabeedi/ourbusiness_sukrabeedi_{rest_mapped}'
            if candidate2 in actual_files:
                return candidate2

    # Strategy 4: /logo/X.png -> /logo/logo_X.png or /images/logo/logo_X.png
    m = re.match(r'^/logo/(.+)$', broken_path)
    if m:
        filename = m.group(1)
        candidates = [
            f'/logo/logo_{filename}',
            f'/images/logo/logo_{filename}',
            f'/images/logo/{filename}',
            f'/logo/{filename}',
        ]
        for c in candidates:
            if c in actual_files:
                return c

    # Strategy 5: /sliding/X -> /images/sliding/X or /logo/X
    m = re.match(r'^/sliding/(.+)$', broken_path)
    if m:
        filename = m.group(1)
        candidates = [
            f'/images/sliding/{filename}',
            f'/sliding/{filename}',
            f'/logo/{filename}',
            f'/images/logo/{filename}',
        ]
        for c in candidates:
            if c in actual_files:
                return c

    # Strategy 6: Basename matching (last resort)
    basename = os.path.basename(broken_path).lower()
    key = '_basename_' + basename
    if key in actual_files:
        return actual_files[key]

    return None

# Step 4: Apply fixes to HTML files
def apply_fixes(mappings):
    """Replace broken paths with correct paths in all HTML files"""
    html_files = glob.glob(os.path.join(ROOT, '*.html')) + \
                 glob.glob(os.path.join(ROOT, 'businesses', '*.html'))

    changes = {}
    for html_file in html_files:
        with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        original = content
        file_changes = []

        for broken, actual in mappings.items():
            if broken in content:
                content = content.replace(broken, actual)
                file_changes.append(f'  {broken} -> {actual}')

        if content != original:
            # Backup
            bak = html_file + '.bak_imgfix'
            if not os.path.exists(bak):
                with open(bak, 'w', encoding='utf-8') as f:
                    f.write(original)

            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)

            rel = os.path.relpath(html_file, ROOT)
            changes[rel] = file_changes

    return changes

# Step 5: For missing files, create nginx rewrite suggestions or symlinks
def handle_missing(missing):
    """Generate report of truly missing files"""
    print("\n=== TRULY MISSING FILES (no match on disk) ===")
    for path, html_files in sorted(missing.items()):
        print(f"  {path}")
        print(f"    used in: {', '.join(html_files)}")

def main():
    print("=== STEP 1: Scanning all media files on disk ===")
    actual_files = get_all_media_files()
    real_files = {k: v for k, v in actual_files.items() if not k.startswith('_basename_')}
    print(f"Found {len(real_files)} media files")

    print("\n=== STEP 2: Finding broken image paths in HTML ===")
    broken_paths = get_broken_paths()
    print(f"Found {len(broken_paths)} broken paths")

    if not broken_paths:
        print("No broken paths found! All images resolve correctly.")
        return

    print("\n=== STEP 3: Mapping broken paths to actual files ===")
    mappings, missing = build_mappings(broken_paths, actual_files)

    print(f"\nMappings found: {len(mappings)}")
    for broken, actual in sorted(mappings.items()):
        print(f"  {broken}")
        print(f"    -> {actual}")

    print(f"\nTruly missing (no match): {len(missing)}")

    print("\n=== STEP 4: Applying fixes to HTML files ===")
    changes = apply_fixes(mappings)

    for html_file, file_changes in sorted(changes.items()):
        print(f"\n{html_file}:")
        for c in file_changes:
            print(c)

    if not changes:
        print("No changes needed (mappings may not appear in any HTML)")

    handle_missing(missing)

    print(f"\n=== SUMMARY ===")
    print(f"Total broken paths: {len(broken_paths)}")
    print(f"Fixed (mapped to actual files): {len(mappings)}")
    print(f"Still missing (need upload or removal): {len(missing)}")

if __name__ == '__main__':
    main()
