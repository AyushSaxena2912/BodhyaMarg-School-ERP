import re

filepath = 'sidebar.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

collapsed_css = """
/* Collapsed Sidebar State */
.sidebar { transition: width 0.3s ease, min-width 0.3s ease; }
.sidebar.collapsed { width: 72px; min-width: 72px; }
.sidebar.collapsed .brand-name { font-size: 0; gap: 0; }
.sidebar.collapsed .brand-name i { font-size: 24px; margin: 0 auto; }
.sidebar.collapsed .school-info, .sidebar.collapsed .school-picker > .ti-chevron-down { display: none; }
.sidebar.collapsed .school-picker { padding: 10px; justify-content: center; }
.sidebar.collapsed .school-icon { margin: 0; }
.sidebar.collapsed .nav-label { display: none; }
.sidebar.collapsed .nav-item { font-size: 0; gap: 0; justify-content: center; padding: 12px 0; }
.sidebar.collapsed .nav-item i { font-size: 20px; margin: 0; }
.sidebar.collapsed .nav-item .ti-chevron-down { display: none; }
.sidebar.collapsed .nav-sub { display: none !important; }
.sidebar.collapsed .nav-sub-container.open > a.nav-item { background: transparent !important; color: var(--text-muted) !important; font-weight: normal !important; }
.sidebar.collapsed .nav-sub-container > a.nav-item.active { background: var(--green-light) !important; color: var(--green) !important; font-weight: 600 !important; }
"""

# Insert collapsed_css before the closing </style>
content = content.replace('</style>', collapsed_css + '\n</style>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated sidebar.html with collapsed CSS")
