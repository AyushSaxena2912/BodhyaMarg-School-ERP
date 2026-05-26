#!/usr/bin/env python3
"""Fix sidebar toggle + active highlight in all ERP HTML files. V3"""

import os, re, glob

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# The OLD sidebar script pattern (inside <aside class="sidebar">)
OLD_SCRIPT_PATTERN = re.compile(
    r'<script>\s*document\.addEventListener\(\'DOMContentLoaded\',\s*function\(\)\s*\{.*?</script>\s*</aside>',
    re.DOTALL
)

# New improved sidebar script
NEW_SCRIPT = r'''<script>
    document.addEventListener('DOMContentLoaded', function() {
      // 1. Detect current page from URL
      var path = window.location.pathname.split('/').pop() || 'index.html';

      // 2. Hide ALL nav-subs first
      document.querySelectorAll('.nav-sub').forEach(function(sub) {
        sub.style.maxHeight = '0';
        sub.style.overflow = 'hidden';
        sub.style.transition = 'max-height 0.25s ease';
      });

      // 3. Reset all chevrons
      document.querySelectorAll('.nav-sub-container').forEach(function(c) {
        c.classList.remove('open');
        var chev = c.querySelector(':scope > a.nav-item .ti-chevron-down');
        if(chev) chev.style.transform = 'rotate(0deg)';
      });

      // 4. Mark active links based on current page URL
      var links = document.querySelectorAll('.sidebar a.nav-item');
      links.forEach(function(link) {
        link.classList.remove('active'); // reset first
        var href = link.getAttribute('href');
        if(href && href !== '#' && href === path) {
          link.classList.add('active');
        }
      });

      // 5. For active items inside sub-containers, also activate parent + expand
      document.querySelectorAll('.nav-sub .nav-item.active').forEach(function(activeItem) {
        var subContainer = activeItem.closest('.nav-sub-container');
        if(subContainer) {
          // Activate parent link
          var parentLink = subContainer.querySelector(':scope > a.nav-item');
          if(parentLink) parentLink.classList.add('active');
          // Expand this sub-menu
          subContainer.classList.add('open');
          var sub = subContainer.querySelector('.nav-sub');
          if(sub) sub.style.maxHeight = sub.scrollHeight + 'px';
          // Rotate chevron
          var chevron = subContainer.querySelector(':scope > a.nav-item .ti-chevron-down');
          if(chevron) chevron.style.transform = 'rotate(180deg)';
        }
      });

      // 6. Highlight parent nav-group labels for active items
      document.querySelectorAll('.nav-item.active').forEach(function(activeItem) {
        var navGroup = activeItem.closest('.nav-group');
        if(navGroup) {
          var label = navGroup.querySelector('.nav-label');
          if(label) label.style.color = 'var(--green)';
        }
      });

      // 7. Click toggle for all sub-containers
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
    });
  </script>
</aside>'''

# CSS to add for active highlighting fix (override link color specificity)
# Including .nav-sub-container.open > a.nav-item so that it is highlighted green when expanded.
CSS_ADDITION = '''
/* Sidebar active state fix - override link color specificity */
.sidebar a.nav-item.active,
.sidebar a.nav-item.active:link,
.sidebar a.nav-item.active:visited,
.sidebar a.nav-item.active:hover,
.nav-sub-container.open > a.nav-item,
.nav-sub-container.open > a.nav-item:link,
.nav-sub-container.open > a.nav-item:visited,
.nav-sub-container.open > a.nav-item:hover {
  background: var(--green-light) !important;
  color: var(--green) !important;
  font-weight: 600 !important;
}
.nav-sub-container > a.nav-item .ti-chevron-down { transition: transform 0.25s ease; }
.nav-sub-container > a.nav-item { user-select: none; }
'''

# Pattern to remove old CSS fix if present
OLD_CSS_FIX = re.compile(
    r'/\*\s*Sidebar active state fix.*?\*/.*?\.nav-sub-container > a\.nav-item \{ user-select: none; \}\s*',
    re.DOTALL
)

count = 0
for filepath in glob.glob(os.path.join(SCRIPT_DIR, '*.html')):
    fname = os.path.basename(filepath)
    # Skip non-sidebar pages
    if fname in ('Login.html', 'Signup.html', 'ForgotPassword.html', 'ResetPassword.html', 
                 'VerifyEmail.html', 'AccountUnderReview.html', 'Success.html', 'index.html'):
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '<aside class="sidebar">' not in content:
        continue
    
    # Replace the old script block
    new_content = OLD_SCRIPT_PATTERN.sub(NEW_SCRIPT, content)
    
    # Remove old CSS fixes if present
    new_content = OLD_CSS_FIX.sub('', new_content)
    
    # Add new CSS fix before the first </style> tag
    if '/* Sidebar active state fix' not in new_content:
        new_content = new_content.replace('</style>', CSS_ADDITION + '</style>', 1)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1
        print(f'✅ Fixed: {fname}')
    else:
        print(f'⏭️  No change: {fname}')

print(f'\nDone! Fixed {count} files.')
