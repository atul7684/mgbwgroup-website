#!/usr/bin/env python3
"""Fix ALL HTML pages: dropdown nav, mobile nav pink bg, nav-dropdown-parent class."""

import os
import glob
import re

# CSS dropdown styles to inject
DROPDOWN_CSS = """
<style>
/* Nav dropdown - hover */
.nav-dropdown-parent { position: relative; }
.nav-dropdown-parent .nav-dropdown-menu {
  display: none;
  position: absolute;
  top: 100%;
  left: 50%;
  transform: translateX(-50%);
  z-index: 50;
  min-width: 260px;
  background: white;
  border-radius: 8px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.15);
  padding: 8px 0;
  margin-top: 2px;
}
.nav-dropdown-parent:hover .nav-dropdown-menu,
.nav-dropdown-parent:focus-within .nav-dropdown-menu {
  display: block;
}
.nav-dropdown-menu a {
  display: block;
  padding: 10px 20px;
  color: #393185;
  text-decoration: none;
  font-size: 14px;
  font-weight: 400;
  transition: background 0.15s;
}
.nav-dropdown-menu a:hover {
  background: #f3f0ff;
}
/* Mobile nav pink background */
@media (max-width: 768px) {
  nav, header nav, [class*="NavigationMenu"], nav[class*="flex"] {
    background: #e8a0b4 !important;
  }
  .nav-dropdown-parent .nav-dropdown-menu {
    position: static;
    transform: none;
    box-shadow: none;
    border-radius: 0;
    min-width: auto;
    background: #f3e0e8;
    margin-top: 0;
    display: none;
  }
  .nav-dropdown-parent:hover .nav-dropdown-menu,
  .nav-dropdown-parent:focus-within .nav-dropdown-menu,
  .nav-dropdown-parent.mobile-open .nav-dropdown-menu {
    display: block;
  }
}
</style>
"""

# Dropdown menu HTML
DROPDOWN_MENU = """<div class="nav-dropdown-menu">
<a href="/businesses/mangalore-ganesh-beedi">Mangalore Ganesh Beedi Works</a>
<a href="/businesses/shukra-beedi">Shukra Beedies LLP</a>
<a href="/businesses/jg-agarbatthi">J&amp;G Agarbathies</a>
<a href="https://silentshoresresort.com/" target="_blank">Silent Shores Resort &amp; Spa</a>
<a href="https://www.instagram.com/mgbwgarage.official" target="_blank">MGBW Garage</a>
</div>"""

# Mobile hamburger + dropdown toggle JS
MOBILE_JS = """<script>
// Mobile hamburger menu
document.addEventListener('DOMContentLoaded', function() {
  var hamburger = document.querySelector('button[class*="inline-flex"][class*="md:hidden"]') ||
                  document.querySelector('button svg[class*="lucide-menu"]')?.closest('button');
  if (hamburger) {
    hamburger.addEventListener('click', function() {
      var nav = document.querySelector('div[data-state]') ||
                document.querySelector('nav div[class*="flex-col"]') ||
                hamburger.closest('nav')?.querySelector('div[class*="hidden"]');
      if (nav) {
        nav.style.display = nav.style.display === 'none' ? 'flex' : 'none';
      }
    });
  }
  // Mobile dropdown toggle
  var ddParent = document.querySelector('.nav-dropdown-parent');
  if (ddParent) {
    var btn = ddParent.querySelector('button');
    if (btn) {
      btn.addEventListener('click', function(e) {
        if (window.innerWidth <= 768) {
          e.preventDefault();
          ddParent.classList.toggle('mobile-open');
        }
      });
    }
  }
});
</script>"""

ROOT = "/var/www/mgbwgroup-static"

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        html = f.read()

    original = html
    fname = os.path.basename(filepath)
    changes = []

    # 1. Remove any existing dropdown CSS/JS we previously injected (clean slate)
    # Remove old style block
    html = re.sub(r'<style>\s*/\* Nav dropdown - hover \*/.*?</style>\s*', '', html, flags=re.DOTALL)
    # Remove old mobile JS
    html = re.sub(r'<script>\s*// Mobile hamburger menu.*?</script>\s*', '', html, flags=re.DOTALL)
    # Remove old dropdown menu divs
    html = re.sub(r'<div class="nav-dropdown-menu">.*?</div>\s*', '', html, flags=re.DOTALL)
    # Remove nav-dropdown-parent class if already added
    html = html.replace(' nav-dropdown-parent', '')

    # 2. Inject CSS before </head>
    if '</head>' in html:
        html = html.replace('</head>', DROPDOWN_CSS + '\n</head>', 1)
        changes.append("Injected CSS dropdown + mobile pink styles")
    else:
        changes.append("WARNING: No </head> found!")

    # 3. Find "Our Businesses" button and add dropdown
    # Look for button with "Our Businesses" text
    button_pattern = r'(<button[^>]*data-state[^>]*>)\s*([\s\S]*?Our\s+Businesses[\s\S]*?)(</button>)'
    match = re.search(button_pattern, html)

    if not match:
        # Try alternative: link or span with "Our Businesses"
        button_pattern2 = r'(<button[^>]*>)\s*([\s\S]*?Our\s+Businesses[\s\S]*?)(</button>)'
        match = re.search(button_pattern2, html)

    if match:
        button_end = match.end()
        # Find parent <li> that contains this button
        # Search backwards from button position for <li
        search_start = max(0, match.start() - 200)
        before_button = html[search_start:match.start()]

        # Find the last <li in the text before button
        li_positions = [m.start() + search_start for m in re.finditer(r'<li\b', before_button)]

        if li_positions:
            li_pos = li_positions[-1]
            # Check if it has class attribute
            li_tag_end = html.index('>', li_pos)
            li_tag = html[li_pos:li_tag_end+1]

            if 'nav-dropdown-parent' not in li_tag:
                if 'class="' in li_tag:
                    html = html[:li_pos] + li_tag.replace('class="', 'class="nav-dropdown-parent ', 1) + html[li_tag_end+1:]
                    changes.append("Added nav-dropdown-parent to existing <li> class")
                elif "class='" in li_tag:
                    html = html[:li_pos] + li_tag.replace("class='", "class='nav-dropdown-parent ", 1) + html[li_tag_end+1:]
                    changes.append("Added nav-dropdown-parent to existing <li> class")
                else:
                    html = html[:li_pos] + '<li class="nav-dropdown-parent"' + html[li_pos+3:li_tag_end+1] + html[li_tag_end+1:]
                    changes.append("Added nav-dropdown-parent class to <li>")

        # Re-find button position (may have shifted)
        match2 = re.search(button_pattern, html) or re.search(button_pattern2, html)
        if match2:
            insert_pos = match2.end()
            html = html[:insert_pos] + '\n' + DROPDOWN_MENU + '\n' + html[insert_pos:]
            changes.append("Inserted dropdown menu after button")
    else:
        changes.append("WARNING: 'Our Businesses' button NOT found!")

    # 4. Inject mobile JS before </body>
    if '</body>' in html:
        html = html.replace('</body>', MOBILE_JS + '\n</body>', 1)
        changes.append("Injected mobile JS")

    # 5. Write file
    if html != original:
        # Backup
        bak = filepath + '.bak_allfix'
        if not os.path.exists(bak):
            with open(bak, 'w', encoding='utf-8') as f:
                f.write(original)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)

        print(f"  FIXED: {filepath} ({len(changes)} changes)")
        for c in changes:
            print(f"    - {c}")
    else:
        print(f"  SKIP: {filepath} (no changes needed)")

# Process all HTML files
html_files = glob.glob(os.path.join(ROOT, "*.html")) + glob.glob(os.path.join(ROOT, "businesses", "*.html"))

print(f"Processing {len(html_files)} HTML files...\n")
for f in sorted(html_files):
    print(f"Processing: {f}")
    try:
        process_file(f)
    except Exception as e:
        print(f"  ERROR: {e}")
    print()

print("DONE! All pages processed.")
