#!/usr/bin/env python3
"""
Fix broken image/video paths in all HTML files.
Handles the Next.js-to-static path conversion where:
  /<dir>/<subdir>/<file> became /<dir>/<dir>_<subdir>_<file> on disk
"""

import os
import re
import glob
from pathlib import Path

ROOT = '/var/www/mgbwgroup-static'

def get_all_media_files():
    extensions = {'.png', '.jpg', '.jpeg', '.webp', '.svg', '.gif', '.mp4', '.ico'}
    files = {}
    for dirpath, dirnames, filenames in os.walk(ROOT):
        for f in filenames:
            full = os.path.join(dirpath, f)
            rel = full[len(ROOT):]
            ext = os.path.splitext(f)[1].lower()
            if ext in extensions:
                files[rel] = full
                basename = f.lower()
                bkey = '_basename_' + basename
                if bkey not in files:
                    files[bkey] = rel
    return files

def get_broken_paths():
    html_files = glob.glob(os.path.join(ROOT, '*.html')) + \
                 glob.glob(os.path.join(ROOT, 'businesses', '*.html'))
    broken = {}
    pattern = re.compile(r'(?:src|poster)=["\'](/[^"\'?#]+\.(?:png|jpg|jpeg|webp|svg|gif|mp4|ico|WEBP|PNG|JPG|JPEG))', re.IGNORECASE)
    for html_file in html_files:
        with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        matches = pattern.findall(content)
        rel_html = os.path.relpath(html_file, ROOT)
        for path in matches:
            full_path = os.path.join(ROOT, path.lstrip('/'))
            if not os.path.exists(full_path):
                broken.setdefault(path, [])
                if rel_html not in broken[path]:
                    broken[path].append(rel_html)
    return broken

def find_actual_path(broken_path, actual_files):
    # 1: Direct match
    if broken_path in actual_files:
        return broken_path

    parts = broken_path.strip('/').split('/')

    # 2: Generic flattening: /<dir>/<sub...>/<file> -> /<dir>/<dir>_<sub>_..._<file>
    if len(parts) >= 3:
        top = parts[0]
        filename = parts[-1]
        middle = '_'.join(parts[1:-1])
        candidates = [
            f'/{top}/{top}_{middle}_{filename}',
            f'/images/{top}/{top}_{middle}_{filename}',
        ]
        # For /images/about/X -> /images/about/images_about_X
        if top == 'images' and len(parts) >= 3:
            sub = parts[1]
            rest_parts = parts[2:]
            if len(rest_parts) == 1:
                candidates.append(f'/images/{sub}/images_{sub}_{rest_parts[0]}')
            else:
                mid2 = '_'.join(rest_parts[:-1])
                candidates.append(f'/images/{sub}/images_{sub}_{mid2}_{rest_parts[-1]}')
        for c in candidates:
            if c in actual_files:
                return c

    # 3: Two-level flattening: /<dir>/<file> -> /<dir>/<dir>_<file>
    if len(parts) == 2:
        top = parts[0]
        fn = parts[1]
        for c in [f'/{top}/{top}_{fn}', f'/images/{top}/{top}_{fn}']:
            if c in actual_files:
                return c

    # 4: /ourbusiness/ -> /business/ with flattening
    m = re.match(r'^/ourbusiness/([^/]+)/(.+)$', broken_path)
    if m:
        biz = m.group(1)
        rest = m.group(2).replace('/', '_')
        # Map spellings
        dir_map = {'ganeshbeedi': 'ganeshbeedi', 'sukrabeedi': 'shukrabeedi'}
        mapped = dir_map.get(biz, biz)
        clean = biz.replace('&amp;', '').replace('&', '')
        tries = [
            f'/business/{mapped}/ourbusiness_{biz}_{rest}',
            f'/business/{mapped}/ourbusiness_{clean}_{rest}',
            f'/business/{mapped}/ourbusiness_{mapped}_{rest}',
            f'/business/{mapped}/ourbusiness_sukrabeedi_{rest}',
            f'/business/{mapped}/ourbusiness_sukrabeedi_{rest.replace("background", "background")}',
        ]
        for c in tries:
            if c in actual_files:
                return c

    # 5: /images/ prefix
    if not broken_path.startswith('/images/'):
        c = '/images' + broken_path
        if c in actual_files:
            return c

    # 6: /logo/ variations
    if broken_path.startswith('/logo/'):
        fn = broken_path[6:]
        for c in [f'/logo/logo_{fn}', f'/images/logo/logo_{fn}',
                   f'/images/logo/{fn}', f'/logo_2/{fn}']:
            if c in actual_files:
                return c

    # 7: /sliding/ -> other locations
    if broken_path.startswith('/sliding/'):
        fn = broken_path[9:]
        for c in [f'/images/sliding/{fn}', f'/logo/{fn}', f'/images/logo/{fn}']:
            if c in actual_files:
                return c

    # 8: Basename match (last resort)
    basename = os.path.basename(broken_path).lower()
    bkey = '_basename_' + basename
    if bkey in actual_files:
        return actual_files[bkey]

    return None

def apply_fixes(mappings):
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
            bak = html_file + '.bak_imgfix'
            if not os.path.exists(bak):
                with open(bak, 'w', encoding='utf-8') as f:
                    f.write(original)
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
            changes[os.path.relpath(html_file, ROOT)] = file_changes
    return changes

def main():
    print("=== Scanning media files ===")
    actual_files = get_all_media_files()
    real = {k: v for k, v in actual_files.items() if not k.startswith('_basename_')}
    print(f"Found {len(real)} media files on disk")

    print("\n=== Finding broken paths ===")
    broken = get_broken_paths()
    print(f"Found {len(broken)} broken paths")
    if not broken:
        print("All images OK!")
        return

    print("\n=== Mapping broken -> actual ===")
    mappings = {}
    missing = {}
    for bp, htmls in broken.items():
        actual = find_actual_path(bp, actual_files)
        if actual:
            mappings[bp] = actual
        else:
            missing[bp] = htmls

    print(f"Mapped: {len(mappings)}")
    for b, a in sorted(mappings.items()):
        print(f"  {b}\n    -> {a}")

    print(f"\n=== Applying {len(mappings)} fixes ===")
    changes = apply_fixes(mappings)
    for f, cs in sorted(changes.items()):
        print(f"\n{f}:")
        for c in cs:
            print(c)

    print(f"\n=== STILL MISSING: {len(missing)} ===")
    for p, htmls in sorted(missing.items()):
        print(f"  {p}  (in: {', '.join(htmls)})")

    print(f"\n=== SUMMARY ===")
    print(f"Total broken: {len(broken)}")
    print(f"Fixed: {len(mappings)}")
    print(f"Missing: {len(missing)}")

if __name__ == '__main__':
    main()
