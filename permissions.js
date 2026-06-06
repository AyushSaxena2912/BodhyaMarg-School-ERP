// BodhyaMarg ERP — Role-Based Auth Engine (permissions.js)
// ============================================================

const BodhyaAuth = {

  // ── DEMO USERS ──────────────────────────────────────────────
  // In production: replace with real backend API call
  DEMO_USERS: [
    { email: 'admin@school.com',    password: 'admin123',    role: 'admin',       name: 'Vikram Sharma',  id: 'USR001' },
    { email: 'teacher@school.com',  password: 'teacher123',  role: 'teacher',     name: 'Mohan Sharma',   id: 'USR002' },
    { email: 'student@school.com',  password: 'student123',  role: 'student',     name: 'Aarav Sharma',   id: 'USR003' },
    { email: 'parent@school.com',   password: 'parent123',   role: 'parent',      name: 'Rajesh Sharma',  id: 'USR004' },
    { email: 'staff@school.com',    password: 'staff123',    role: 'staff',       name: 'Priya Kumari',   id: 'USR005' },
    { email: 'superadmin@school.com', password: 'super123',  role: 'superadmin',  name: 'System Admin',   id: 'USR006' },
  ],

  // ── SESSION MANAGEMENT ──────────────────────────────────────
  login: function(role, name, id) {
    localStorage.setItem('bodhya_user_role', role);
    localStorage.setItem('bodhya_user_name', name);
    localStorage.setItem('bodhya_user_id',   id || 'USR000');
    localStorage.setItem('bodhya_logged_in', 'true');
    window.location.href = this.getDashboard(role);
  },

  logout: function() {
    localStorage.removeItem('bodhya_user_role');
    localStorage.removeItem('bodhya_user_name');
    localStorage.removeItem('bodhya_user_id');
    localStorage.removeItem('bodhya_logged_in');
    window.location.href = 'Login.html';
  },

  isLoggedIn: function() {
    return localStorage.getItem('bodhya_logged_in') === 'true';
  },

  getUser: function() {
    return {
      role:  localStorage.getItem('bodhya_user_role') || 'guest',
      name:  localStorage.getItem('bodhya_user_name') || 'User',
      id:    localStorage.getItem('bodhya_user_id')   || '',
    };
  },

  // Legacy support — still used by sidebar.js
  getRole: function() {
    return this.getUser().role;
  },

  setRole: function(role) {
    localStorage.setItem('bodhya_user_role', role);
  },

  // ── ROLE → DASHBOARD ROUTING ────────────────────────────────
  getDashboard: function(role) {
    const map = {
      admin:       'VehicleOccupancy.html',
      superadmin:  'RolesPermissions.html',
      teacher:     'TeacherWorkspace.html',
      student:     'StudentReportCard.html',
      parent:      'SearchExamResults.html',
      staff:       'StaffAttendance.html',
    };
    return map[role] || 'Login.html';
  },

  // ── PAGE GUARD ──────────────────────────────────────────────
  // Call this at the top of every protected page:
  //   BodhyaAuth.guardPage(['admin','teacher']);
  guardPage: function(allowedRoles) {
    // If not logged in → send to login
    if (!this.isLoggedIn()) {
      window.location.href = 'Login.html';
      return;
    }
    const role = this.getRole();
    if (allowedRoles && allowedRoles.length > 0) {
      // Allow superadmin and admin to view all pages
      if (role === 'superadmin' || role === 'admin') {
        return;
      }
      
      if (!allowedRoles.includes(role)) {
        // Redirect to their own dashboard instead of an error page
        window.location.href = this.getDashboard(role);
      }
    }
  },

  // ── CREDENTIAL VERIFICATION (Demo / Mock) ───────────────────
  verify: function(email, password) {
    const user = this.DEMO_USERS.find(
      u => u.email.toLowerCase() === email.toLowerCase() && u.password === password
    );
    return user || null;
  },

  // ── ROLE LABEL ──────────────────────────────────────────────
  getRoleLabel: function(role) {
    const labels = {
      admin:      'Administrator',
      superadmin: 'Super Admin',
      teacher:    'Teacher',
      student:    'Student',
      parent:     'Parent / Guardian',
      staff:      'Staff Member',
    };
    return labels[role] || 'User';
  },

  getRoleIcon: function(role) {
    const icons = {
      admin:      'ti-shield-check',
      superadmin: 'ti-shield-star',
      teacher:    'ti-chalkboard',
      student:    'ti-school',
      parent:     'ti-user-heart',
      staff:      'ti-briefcase',
    };
    return icons[role] || 'ti-user';
  },

  getRoleColor: function(role) {
    const colors = {
      admin:      '#1a7a4a',
      superadmin: '#7c3aed',
      teacher:    '#0284c7',
      student:    '#059669',
      parent:     '#d97706',
      staff:      '#64748b',
    };
    return colors[role] || '#64748b';
  },

  // Hides elements that have data-allowed-roles attribute
  applyRoleRestrictions: function() {
    const currentRole = this.getRole().toLowerCase();
    document.querySelectorAll('[data-allowed-roles]').forEach(el => {
      const allowed = el.getAttribute('data-allowed-roles').split(',').map(r => r.trim().toLowerCase());
      
      // Allow superadmin and admin to see all elements
      if (currentRole === 'superadmin' || currentRole === 'admin') {
        return;
      }
      
      if (!allowed.includes(currentRole)) {
        el.style.display = 'none';
      }
    });
  },

  // ── CMS CONFIGURATION APPLICATION ───────────────────────────
  applyCMS: function(overrideRole) {
    const saved = localStorage.getItem('bodhya_cms_config');
    if (!saved) return;
    try {
      const config = JSON.parse(saved);
      
      // 1. Logo
      const logoEl = document.querySelector('.header .school-logo');
      if (logoEl && config.logoUrl) {
        logoEl.src = config.logoUrl;
      }
      
      // 2. Titles
      const nameEl = document.querySelector('.header .school-name');
      if (nameEl && config.schoolName) nameEl.textContent = config.schoolName;
      
      const subEl = document.querySelector('.header .school-sub');
      if (subEl && config.schoolSub) subEl.textContent = config.schoolSub;
      
      const sub2El = document.querySelector('.header .school-sub2');
      if (sub2El && config.schoolSub2) sub2El.textContent = config.schoolSub2;
      
      // 3. Navigation links
      const navEl = document.querySelector('.header-nav');
      if (navEl && config.navLinks && config.navLinks.length > 0) {
        navEl.innerHTML = config.navLinks.map(link => `<a href="${link.url}">${link.title}</a>`).join('');
      }
      
      // 4. Banner image
      const bannerImg = document.querySelector('.banner-section img');
      if (bannerImg) {
        const role = (overrideRole || localStorage.getItem('bodhya_user_role') || 'guest').toLowerCase();
        if (role === 'admin' && config.adminBannerUrl) {
          bannerImg.src = config.adminBannerUrl;
        } else if (role === 'superadmin' && config.superadminBannerUrl) {
          bannerImg.src = config.superadminBannerUrl;
        } else if (config.defaultBannerUrl) {
          bannerImg.src = config.defaultBannerUrl;
        }
      }
    } catch (e) {
      console.error('Error applying CMS configs:', e);
    }
  }
};

// Auto-apply element restrictions and CMS config on DOMContentLoaded
document.addEventListener('DOMContentLoaded', () => {
  BodhyaAuth.applyRoleRestrictions();
  BodhyaAuth.applyCMS();
});
