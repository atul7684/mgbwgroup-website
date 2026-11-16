#!/usr/bin/env python3
"""
Fix "Our Businesses" dropdown with CSS hover approach (no click needed).
Replaces the JS-based approach which had event propagation issues.
Also adds a small inline JS for mobile hamburger menu.
"""
import shutil, re

SRC = '/var/www/mgbwgroup-static/index.html'
BAK = '/var/www/mgbwgroup-static/index.html.bak7'

html = open(SRC).read()
print(f"File: {len(html)} chars")
shutil.copy2(SRC, BAK)

# Step 1: Remove old injected script (from fix_dropdown.py)
old_script_start = html.find('<script>\ndocument.addEventListener(\'DOMContentLoaded\'')
if old_script_start < 0:
    old_script_start = html.find('<script>\r\ndocument.addEventListener(\'DOMContentLoaded\'')
if old_script_start >= 0:
    old_script_end = html.find('</script>', old_script_start)
    if old_script_end >= 0:
        old_script_end += len('</script>')
        removed = html[old_script_start:old_script_end]
        html = html[:old_script_start] + html[old_script_end:]
        print(f"Removed old script: {len(removed)} chars")
    else:
        print("WARNING: Found script start but no end tag")
else:
    print("No old script found (OK if first run)")

# Step 2: Inject CSS-based hover dropdown styles into head
# Find the </head> tag to add styles
css_dropdown = '''
<style>
/* Our Businesses dropdown - CSS hover */
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
</style>
'''

head_close = html.find('</head>')
if head_close >= 0:
    html = html[:head_close] + css_dropdown + '\n' + html[head_close:]
    print(f"Injected CSS dropdown styles before </head>")
else:
    print("ERROR: No </head> found")

# Step 3: Find the "Our Businesses" button's parent <li> and add class + dropdown menu
# The button looks like: <button ... data-state="closed" ...>Our Businesses
# Its parent is an <li>

# Find the button
btn_pattern = r'(<button[^>]*data-state="closed"[^>]*>)'
btn_match = re.search(btn_pattern, html)
if btn_match:
    btn_tag = btn_match.group(1)
    btn_pos = btn_match.start()
    print(f"Found trigger button at char {btn_pos}")

    # Find parent <li> before this button
    # Search backward for <li
    search_back = html[:btn_pos]
    li_pos = search_back.rfind('<li')
    if li_pos >= 0:
        # Find the end of this <li tag (the >)
        li_tag_end = html.find('>', li_pos) + 1
        old_li_tag = html[li_pos:li_tag_end]
        print(f"Found parent <li> at char {li_pos}: {old_li_tag[:60]}...")

        # Add class to <li>
        if 'class="' in old_li_tag:
            new_li_tag = old_li_tag.replace('class="', 'class="nav-dropdown-parent ')
        else:
            new_li_tag = old_li_tag.replace('<li', '<li class="nav-dropdown-parent"', 1)

        html = html[:li_pos] + new_li_tag + html[li_tag_end:]
        print(f"Added nav-dropdown-parent class to <li>")

        # Now find position right after the button closing tag to insert dropdown menu
        # The button text is "Our Businesses" followed by SVG chevron, then </button>
        btn_close = html.find('</button>', btn_pos)
        if btn_close >= 0:
            btn_close += len('</button>')

            dropdown_menu = '''
<div class="nav-dropdown-menu">
<a href="/businesses/mangalore-ganesh-beedi">Mangalore Ganesh Beedi Works</a>
<a href="/businesses/shukra-beedi">Shukra Beedies LLP</a>
<a href="/businesses/jg-agarbatthi">J&amp;G Agarbathies</a>
<a href="https://silentshoresresort.com/" target="_blank">Silent Shores Resort &amp; Spa</a>
<a href="https://www.instagram.com/mgbwgarage.official" target="_blank">MGBW Garage</a>
</div>'''

            # Check if there's already a nav-dropdown-menu (from previous run)
            if 'nav-dropdown-menu' not in html[btn_close:btn_close+500]:
                html = html[:btn_close] + dropdown_menu + html[btn_close:]
                print(f"Inserted dropdown menu after </button> at char {btn_close}")
            else:
                print("Dropdown menu already present, skipping insert")
        else:
            print("ERROR: Could not find </button> close tag")
    else:
        print("ERROR: Could not find parent <li> for button")
else:
    print("ERROR: Could not find trigger button with data-state")

# Step 4: Add minimal JS for mobile hamburger (the CSS dropdown handles desktop)
mobile_js = '''
<script>
(function(){
  // Mobile hamburger toggle
  var hamburger = document.querySelector('button.xl\\\\:hidden, button[class*="xl:hidden"]');
  if (!hamburger) {
    var btns = document.querySelectorAll('button');
    for (var i = 0; i < btns.length; i++) {
      if (btns[i].querySelector('.sr-only') || btns[i].textContent.trim() === 'Open menu') {
        hamburger = btns[i];
        break;
      }
    }
  }
  if (hamburger) {
    var nav = document.querySelector('nav[aria-label="Main"]') || document.querySelector('nav ul');
    if (nav) {
      // On mobile, the nav list is hidden by md:flex or similar
      hamburger.addEventListener('click', function() {
        var isHidden = nav.style.display === 'none' || nav.style.display === '';
        if (isHidden) {
          nav.style.display = 'flex';
          nav.style.flexDirection = 'column';
          nav.style.position = 'absolute';
          nav.style.top = '60px';
          nav.style.left = '0';
          nav.style.right = '0';
          nav.style.background = 'white';
          nav.style.padding = '16px';
          nav.style.zIndex = '100';
          nav.style.boxShadow = '0 4px 20px rgba(0,0,0,0.1)';
        } else {
          nav.style.display = '';
          nav.style.flexDirection = '';
          nav.style.position = '';
          nav.style.top = '';
          nav.style.left = '';
          nav.style.right = '';
          nav.style.background = '';
          nav.style.padding = '';
          nav.style.zIndex = '';
          nav.style.boxShadow = '';
        }
      });
    }
  }
})();
</script>
'''

body_close = html.rfind('</body>')
if body_close >= 0:
    html = html[:body_close] + mobile_js + '\n' + html[body_close:]
    print(f"Injected mobile hamburger JS before </body>")
else:
    print("WARNING: No </body> found")

open(SRC, 'w').write(html)
print(f"Final: {len(html)} chars")
print("DONE!")
