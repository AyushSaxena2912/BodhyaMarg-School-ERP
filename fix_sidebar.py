#!/usr/bin/env python3
"""Fix sidebar toggle + active highlight in all ERP HTML files."""

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
      // 1. Detect current page
      var path = window.location.pathname.split('/').pop() || 'index.html';

      // 2. Mark active links
      var links = document.querySelectorAll('.sidebar a.nav-item');
      links.forEach(function(link) {
        var href = link.getAttribute('href');
        if(href && href !== '#' && href === path) {
          link.classList.add('active');
          // Also mark parent nav-item in the sub-container
          var subContainer = link.closest('.nav-sub-container');
          if(subContainer) {
            var parentLink = subContainer.querySelector(':scope > a.nav-item');
            if(parentLink) parentLink.classList.add('active');
          }
        }
      });

      // 3. Hide all nav-subs first
      document.querySelectorAll('.nav-sub').forEach(function(sub) {
        sub.style.maxHeight = '0';
        sub.style.overflow = 'hidden';
        sub.style.transition = 'max-height 0.25s ease';
      });

      // 4. Open nav-subs that contain active items
      document.querySelectorAll('.nav-item.active').forEach(function(activeItem) {
        var subContainer = activeItem.closest('.nav-sub-container');
        if(subContainer) {
          subContainer.classList.add('open');
          var sub = subContainer.querySelector('.nav-sub');
          if(sub) sub.style.maxHeight = sub.scrollHeight + 'px';
          // Rotate chevron
          var chevron = subContainer.querySelector(':scope > a.nav-item .ti-chevron-down');
          if(chevron) chevron.style.transform = 'rotate(180deg)';
        }
        // Highlight parent nav-group label
        var navGroup = activeItem.closest('.nav-group');
        if(navGroup) {
          var label = navGroup.querySelector('.nav-label');
          if(label) label.style.color = 'var(--green)';
        }
      });

      // 5. Add click toggle for all sub-containers
      document.querySelectorAll('.nav-sub-container').forEach(function(container) {
        var parentLink = container.querySelector(':scope > a.nav-item');
        if(!parentLink) return;

        parentLink.addEventListener('click', function(e) {
          // If the parent link has a real href and is the active page, allow navigation
          // Otherwise, toggle the submenu
          var href = parentLink.getAttribute('href');
          var sub = container.querySelector('.nav-sub');
          if(!sub) return;

          e.preventDefault();
          e.stopPropagation();

          var isOpen = container.classList.contains('open');
          
          if(isOpen) {
            // Close it
            container.classList.remove('open');
            sub.style.maxHeight = '0';
            var chevron = parentLink.querySelector('.ti-chevron-down');
            if(chevron) chevron.style.transform = 'rotate(0deg)';
          } else {
            // Open it
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

# CSS to add for chevron transition
CSS_ADDITION = '''
.nav-sub-container > a.nav-item .ti-chevron-down { transition: transform 0.25s ease; }
.nav-sub-container > a.nav-item { user-select: none; }
'''

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
    
    # Add chevron CSS if not already there
    if 'ti-chevron-down' not in content.split('</style>')[0] or 'transition: transform' not in content:
        # Add CSS before the first </style> tag
        new_content = new_content.replace('</style>', CSS_ADDITION + '</style>', 1)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1
        print(f'✅ Fixed: {fname}')
    else:
        print(f'⏭️  No change: {fname}')

print(f'\nDone! Fixed {count} files.')
