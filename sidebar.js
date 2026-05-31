document.addEventListener('DOMContentLoaded', function() {
  fetch('sidebar.html')
    .then(response => response.text())
    .then(html => {
      var container = document.getElementById('sidebar-container');
      if (container) {
        container.outerHTML = html;
        initSidebar();
        applySidebarRoleFilters();
      }
    })
    .catch(err => console.error('Failed to load sidebar:', err));
});

function applySidebarRoleFilters() {
  const currentRole = (localStorage.getItem('bodhya_user_role') || 'admin').toLowerCase();
  document.body.setAttribute('data-current-role', currentRole);
  
  const switcher = document.getElementById('sidebarRoleSwitcher');
  if (switcher) switcher.value = currentRole;
  
  // Wait a tick for CSS to apply, then hide empty nav-groups
  setTimeout(() => {
    document.querySelectorAll('.sidebar .nav-group').forEach(group => {
      const visibleLinks = Array.from(group.querySelectorAll('.nav-item')).filter(link => {
        return window.getComputedStyle(link).display !== 'none' && 
               window.getComputedStyle(link.closest('.nav-sub-container') || link).display !== 'none';
      });
      if (visibleLinks.length === 0) {
        group.style.display = 'none';
      }
    });
  }, 10);
}

function initSidebar() {
  // Get path and remove .html for Netlify clean URLs
  var rawPath = window.location.pathname.split('/').pop();
  var cleanPath = rawPath.replace(/\.html$/, '').toLowerCase();
  if (!cleanPath || cleanPath === '') cleanPath = 'index'; // Handle root url

  // Sidebar Toggle Logic
  var toggleBtn = document.querySelector('.ti-menu-2');
  var sidebar = document.querySelector('.sidebar');
  if(toggleBtn && sidebar) {
    toggleBtn.addEventListener('click', function() {
      sidebar.classList.toggle('collapsed');
      if(sidebar.classList.contains('collapsed')) {
        localStorage.setItem('sidebarState', 'collapsed');
      } else {
        localStorage.setItem('sidebarState', 'expanded');
      }
    });

    // Check saved state
    if(localStorage.getItem('sidebarState') === 'collapsed') {
      sidebar.classList.add('collapsed');
    }
  }

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
    if(href && href !== '#') {
      var cleanHref = href.split('/').pop().replace(/\.html$/, '').toLowerCase();
      if(cleanHref === cleanPath) {
        link.classList.add('active');
      }
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
