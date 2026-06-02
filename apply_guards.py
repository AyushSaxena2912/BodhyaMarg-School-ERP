import os

guards = {
    'AllStudents.html': "['admin']",
    'AddStudent.html': "['admin']",
    'AllTeachers.html': "['admin']",
    'AddTeacher.html': "['admin']",
    'ExamResults.html': "['admin', 'teacher']",
    'StudentAttendance.html': "['admin', 'teacher']",
    'TeacherWorkspace.html': "['teacher']",
    'StudentReportCard.html': "['admin', 'teacher', 'student', 'parent']",
    'SearchExamResults.html': "['admin', 'teacher', 'student', 'parent']",
    'StaffAttendance.html': "['admin', 'staff']",
    'RolesPermissions.html': "['admin', 'superadmin']",
    'Leave.html': "['admin', 'teacher', 'staff']",
    'LeaveApproveRequest.html': "['admin', 'teacher', 'staff']"
}

def apply_guard(filepath, guard_roles):
    with open(filepath, 'r') as f:
        content = f.read()
    
    if "BodhyaAuth.guardPage" in content:
        return
        
    script_str = f'<script src="permissions.js"></script>\n<script>BodhyaAuth.guardPage({guard_roles});</script>\n'
    
    # We will insert it just before </head> or just after <body>
    if '</head>' in content:
        content = content.replace('</head>', script_str + '</head>')
    else:
        # fallback
        content = script_str + content
        
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Applied guard to {filepath}")

for root, _, files in os.walk('.'):
    for file in files:
        if file in guards:
            apply_guard(os.path.join(root, file), guards[file])
