#!/usr/bin/env python3
"""
Fix the "Our Businesses" dropdown and hamburger menu.
Since Next.js/React JS is stripped, we add vanilla JS to handle:
1. "Our Businesses" desktop dropdown toggle
2. Mobile hamburger menu toggle
"""
import shutil

SRC = '/var/www/mgbwgroup-static/index.html'
BAK = '/var/www/mgbwgroup-static/index.html.bak6'

html = open(SRC).read()
print(f"File: {len(html)} chars")
shutil.copy2(SRC, BAK)

# The dropdown script to inject
dropdown_js = '''
<script>
document.addEventListener('DOMContentLoaded', function() {
  // 1. Fix "Our Businesses" dropdown
  var triggerBtn = document.querySelector('button[data-state]');
  if (triggerBtn) {
    // Create dropdown content
    var businesses = [
      {name: 'Mangalore Ganesh Beedi Works', href: '/businesses/mangalore-ganesh-beedi'},
      {name: 'Shukra Beedies LLP', href: '/businesses/shukra-beedi'},
      {name: 'J&G Agarbathies', href: '/businesses/jg-agarbatthi'},
      {name: 'Silent Shores Resort & Spa', href: 'https://silentshoresresort.com/'},
      {name: 'MGBW Garage', href: 'https://www.instagram.com/mgbwgarage.official'}
    ];

    var dropdown = document.createElement('div');
    dropdown.style.cssText = 'display:none;position:absolute;top:100%;left:0;z-index:50;min-width:250px;background:white;border-radius:8px;box-shadow:0 4px 20px rgba(0,0,0,0.15);padding:8px 0;margin-top:4px;';

    businesses.forEach(function(biz) {
      var a = document.createElement('a');
      a.href = biz.href;
      a.textContent = biz.name;
      a.style.cssText = 'display:block;padding:10px 20px;color:#393185;text-decoration:none;font-size:14px;';
      a.addEventListener('mouseenter', function() { this.style.background = '#f3f0ff'; });
      a.addEventListener('mouseleave', function() { this.style.background = 'transparent'; });
      if (biz.href.startsWith('http')) a.target = '_blank';
      dropdown.appendChild(a);
    });

    triggerBtn.parentElement.appendChild(dropdown);
    triggerBtn.parentElement.style.position = 'relative';

    triggerBtn.addEventListener('click', function(e) {
      e.stopPropagation();
      var isOpen = dropdown.style.display !== 'none';
      dropdown.style.display = isOpen ? 'none' : 'block';
      triggerBtn.setAttribute('data-state', isOpen ? 'closed' : 'open');
      triggerBtn.setAttribute('aria-expanded', isOpen ? 'false' : 'true');
    });

    document.addEventListener('click', function() {
      dropdown.style.display = 'none';
      triggerBtn.setAttribute('data-state', 'closed');
      triggerBtn.setAttribute('aria-expanded', 'false');
    });
  }

  // 2. Fix hamburger menu (mobile)
  var hamburger = document.querySelector('button[class*="inline-flex"][class*="md:hidden"], button.inline-flex.items-center.justify-center.whitespace-nowrap');
  // Find hamburger by looking for the SVG menu icon button
  if (!hamburger) {
    var allBtns = document.querySelectorAll('button');
    for (var i = 0; i < allBtns.length; i++) {
      var btn = allBtns[i];
      if (btn.querySelector('svg') && btn.textContent.trim() === '' && btn !== triggerBtn) {
        // Check if it has sr-only text "Toggle Menu" or similar
        var srText = btn.querySelector('.sr-only');
        if (srText || btn.getAttribute('aria-label')) {
          hamburger = btn;
          break;
        }
      }
    }
  }

  if (hamburger) {
    // Find the mobile nav panel - usually a div with mobile nav links
    var mobileNav = document.querySelector('[class*="md:hidden"][class*="absolute"], [class*="mobile-menu"]');

    // If no mobile nav panel found, create one from desktop nav
    if (!mobileNav) {
      var desktopLinks = document.querySelectorAll('nav a[href], nav button[data-state]');
      mobileNav = document.createElement('div');
      mobileNav.style.cssText = 'display:none;position:fixed;top:0;left:0;right:0;bottom:0;background:white;z-index:100;padding:80px 20px 20px;overflow-y:auto;';

      // Close button
      var closeBtn = document.createElement('button');
      closeBtn.innerHTML = '&times;';
      closeBtn.style.cssText = 'position:absolute;top:20px;right:20px;font-size:32px;background:none;border:none;cursor:pointer;color:#393185;';
      closeBtn.addEventListener('click', function() { mobileNav.style.display = 'none'; });
      mobileNav.appendChild(closeBtn);

      desktopLinks.forEach(function(link) {
        var text = link.textContent.trim();
        if (!text || text.length > 40) return;

        if (link.tagName === 'BUTTON') {
          // "Our Businesses" - add as heading + sub-links
          var heading = document.createElement('div');
          heading.textContent = text;
          heading.style.cssText = 'padding:12px 0;font-weight:bold;color:#393185;font-size:18px;border-bottom:1px solid #eee;';
          mobileNav.appendChild(heading);

          businesses.forEach(function(biz) {
            var a = document.createElement('a');
            a.href = biz.href;
            a.textContent = biz.name;
            a.style.cssText = 'display:block;padding:10px 0 10px 20px;color:#393185;text-decoration:none;font-size:16px;';
            if (biz.href.startsWith('http')) a.target = '_blank';
            mobileNav.appendChild(a);
          });
        } else {
          var a = document.createElement('a');
          a.href = link.href;
          a.textContent = text;
          a.style.cssText = 'display:block;padding:12px 0;color:#393185;text-decoration:none;font-size:18px;border-bottom:1px solid #eee;';
          mobileNav.appendChild(a);
        }
      });

      document.body.appendChild(mobileNav);
    }

    hamburger.addEventListener('click', function() {
      mobileNav.style.display = mobileNav.style.display === 'none' ? 'block' : 'none';
    });
  }
});
</script>
'''

# Inject before </body>
body_close = html.rfind('</body>')
if body_close < 0:
    body_close = html.rfind('</html>')
if body_close < 0:
    body_close = len(html)

html = html[:body_close] + dropdown_js + '\n' + html[body_close:]
print(f"Injected dropdown JS before </body> at char {body_close}")

open(SRC, 'w').write(html)
print(f"Final: {len(html)} chars")
print("DONE!")
