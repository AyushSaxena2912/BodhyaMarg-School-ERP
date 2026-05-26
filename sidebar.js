document.addEventListener('DOMContentLoaded', function() {
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
