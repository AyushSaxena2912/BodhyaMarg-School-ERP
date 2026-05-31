// Role-Based Access Control Engine for BodhyaMarg ERP

const BodhyaAuth = {
  // Get current user role (defaults to admin if none set)
  getRole: function() {
    return localStorage.getItem('bodhya_user_role') || 'admin';
  },

  // Set current user role
  setRole: function(role) {
    localStorage.setItem('bodhya_user_role', role);
  },

  // Hide or disable elements based on their data-allowed-roles attribute
  // Example: <button data-allowed-roles="admin,teacher">Edit</button>
  applyRoleRestrictions: function() {
    const currentRole = this.getRole();
    const restrictedElements = document.querySelectorAll('[data-allowed-roles]');
    
    restrictedElements.forEach(el => {
      const allowedRoles = el.getAttribute('data-allowed-roles').split(',').map(r => r.trim().toLowerCase());
      if (!allowedRoles.includes(currentRole.toLowerCase())) {
        el.style.display = 'none'; // Hide the element completely
        // Optionally, if we just want to disable inputs instead of hiding:
        // if (el.tagName === 'INPUT' || el.tagName === 'BUTTON' || el.tagName === 'SELECT' || el.tagName === 'TEXTAREA') {
        //   el.disabled = true;
        // }
      }
    });
  },

  // Map of which role lands on which dashboard upon login
  getDashboardForRole: function(role) {
    switch (role) {
      case 'admin':
        return 'VehicleOccupancy.html'; // Or whatever the main admin dashboard is
      case 'teacher':
        return 'ExamSchedule.html'; // Example dashboard for teacher
      case 'student':
        return 'StudentReportCard.html'; // Example dashboard for student
      default:
        return 'VehicleOccupancy.html';
    }
  }
};

// Auto-run restrictions on page load if elements exist
document.addEventListener('DOMContentLoaded', () => {
  BodhyaAuth.applyRoleRestrictions();
});
