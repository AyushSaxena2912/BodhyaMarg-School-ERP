#!/usr/bin/env python3
"""Migrate ERP HTML files to use a dynamic JavaScript fetch for the sidebar."""

import os, re, glob

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# 1. Read ClassRoutine.html to get the sidebar structure
with open(os.path.join(SCRIPT_DIR, 'ClassRoutine.html'), 'r', encoding='utf-8') as f:
    class_routine = f.read()

# Extract the <aside class="sidebar"> block but remove the <script> part inside it
aside_match = re.search(r'(<aside class="sidebar">.*?)<script>', class_routine, re.DOTALL)
if aside_match:
    sidebar_html_content = aside_match.group(1).strip() + '\n</aside>'
else:
    print("Could not find sidebar in ClassRoutine.html")
    exit(1)

# Add the CSS block to the sidebar.html
sidebar_html_full = f'''<style>
/* Sidebar active state fix - override link color specificity */
.sidebar a.nav-item.active,
.sidebar a.nav-item.active:link,
.sidebar a.nav-item.active:visited,
.sidebar a.nav-item.active:hover,
.nav-sub-container.open > a.nav-item,
.nav-sub-container.open > a.nav-item:link,
.nav-sub-container.open > a.nav-item:visited,
.nav-sub-container.open > a.nav-item:hover {{
  background: var(--green-light) !important;
  color: var(--green) !important;
  font-weight: 600 !important;
}}
.nav-sub-container > a.nav-item .ti-chevron-down {{ transition: transform 0.25s ease; }}
.nav-sub-container > a.nav-item {{ user-select: none; }}

/* Highlight Nav Label if it has an active or open item */
.nav-group:has(.nav-item.active) .nav-label,
.nav-group:has(.nav-sub-container.open) .nav-label {{
  color: var(--green) !important;
}}
</style>

{sidebar_html_content}
'''

with open(os.path.join(SCRIPT_DIR, 'sidebar.html'), 'w', encoding='utf-8') as f:
    f.write(sidebar_html_full)

# 2. Write sidebar.js
sidebar_js_content = '''document.addEventListener('DOMContentLoaded', function() {
  fetch('sidebar.html')
    .then(response => response.text())
    .then(html => {
      var container = document.getElementById('sidebar-container');
      if (container) {
        container.outerHTML = html;
        initSidebar();
      }
    })
    .catch(err => console.error('Failed to load sidebar:', err));
});

function initSidebar() {
  var path = window.location.pathname.split('/').pop() || 'index.html';

  document.querySelectorAll('.nav-sub').forEach(function(sub) {
    sub.style.maxHeight = '0';
    sub.style.overflow = 'hidden';
    sub.style.transition = 'max-height 0.25s ease';
  });

  document.querySelectorAll('.nav-sub-container').forEach(function(c) {
    c.classList.remove('open');
    var chev = c.querySelector(':scope > a.nav-item .ti-chevron-down');
    if(chev) chev.style.transform = 'rotate(0deg)';
  });

  var links = document.querySelectorAll('.sidebar a.nav-item');
  links.forEach(function(link) {
    link.classList.remove('active');
    var href = link.getAttribute('href');
    if(href && href !== '#' && href === path) {
      link.classList.add('active');
    }
  });

  document.querySelectorAll('.nav-sub .nav-item.active').forEach(function(activeItem) {
    var subContainer = activeItem.closest('.nav-sub-container');
    if(subContainer) {
      var parentLink = subContainer.querySelector(':scope > a.nav-item');
      if(parentLink) parentLink.classList.add('active');
      subContainer.classList.add('open');
      var sub = subContainer.querySelector('.nav-sub');
      if(sub) sub.style.maxHeight = sub.scrollHeight + 'px';
      var chevron = subContainer.querySelector(':scope > a.nav-item .ti-chevron-down');
      if(chevron) chevron.style.transform = 'rotate(180deg)';
    }
  });

  document.querySelectorAll('.nav-sub-container').forEach(function(container) {
    var parentLink = container.querySelector(':scope > a.nav-item');
    if(!parentLink) return;
    parentLink.addEventListener('click', function(e) {
      var sub = container.querySelector('.nav-sub');
      if(!sub) return;
      e.preventDefault();
      e.stopPropagation();

      var isOpen = container.classList.contains('open');
      if(isOpen) {
        container.classList.remove('open');
        sub.style.maxHeight = '0';
        var chevron = parentLink.querySelector('.ti-chevron-down');
        if(chevron) chevron.style.transform = 'rotate(0deg)';
      } else {
        container.classList.add('open');
        sub.style.maxHeight = sub.scrollHeight + 'px';
        var chevron = parentLink.querySelector('.ti-chevron-down');
        if(chevron) chevron.style.transform = 'rotate(180deg)';
      }
    });
  });
}
'''
with open(os.path.join(SCRIPT_DIR, 'sidebar.js'), 'w', encoding='utf-8') as f:
    f.write(sidebar_js_content)

# 3. Process all HTML files
OLD_CSS_FIX_1 = re.compile(r'/\*\s*Sidebar active state fix.*?\*/.*?\.nav-sub-container > a\.nav-item \{ user-select: none; \}\s*', re.DOTALL)
OLD_CSS_FIX_2 = re.compile(r'/\*\s*Highlight Nav Label.*?\*/.*?color: var\(--green\) !important;\s*\}\s*', re.DOTALL)
STYLE_CLEAN = re.compile(r'<style>\s*</style>', re.DOTALL)

count = 0
for filepath in glob.glob(os.path.join(SCRIPT_DIR, '*.html')):
    fname = os.path.basename(filepath)
    if fname in ('Login.html', 'Signup.html', 'ForgotPassword.html', 'ResetPassword.html', 
                 'VerifyEmail.html', 'AccountUnderReview.html', 'Success.html', 'index.html', 'sidebar.html'):
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '<aside class="sidebar">' not in content and 'id="sidebar-container"' not in content:
        continue
    
    new_content = content
    
    # Remove old inline CSS fixes if any
    new_content = OLD_CSS_FIX_1.sub('', new_content)
    new_content = OLD_CSS_FIX_2.sub('', new_content)
    new_content = STYLE_CLEAN.sub('', new_content)
    
    # Replace aside
    new_content = re.sub(
        r'<!-- Unified Sidebar -->\s*<aside class="sidebar">.*?</aside>',
        '<div id="sidebar-container"></div>',
        new_content,
        flags=re.DOTALL
    )
    new_content = re.sub(
        r'<aside class="sidebar">.*?</aside>',
        '<div id="sidebar-container"></div>',
        new_content,
        flags=re.DOTALL
    )

    # Insert script before </body>
    if 'src="sidebar.js"' not in new_content:
        new_content = new_content.replace('</body>', '<script src="sidebar.js"></script>\n</body>')
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1
        print(f'✅ Converted: {fname}')
    else:
        print(f'⏭️  No change: {fname}')

print(f'\\nDone! Converted {count} files to use JS fetch for sidebar.')
