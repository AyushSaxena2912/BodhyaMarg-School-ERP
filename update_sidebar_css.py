import os

filepath = 'sidebar.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# The CSS to inject
full_sidebar_css = """
/* Definitive Sidebar CSS */
.sidebar { width: 224px; min-width: 224px; background: var(--white); border-right: 1px solid var(--border); display: flex; flex-direction: column; overflow-y: auto; height: 100vh; }
.sidebar::-webkit-scrollbar { width: 4px; }
.sidebar::-webkit-scrollbar-thumb { background: var(--border); border-radius: 4px; }
.sidebar a, .sidebar a:link, .sidebar a:visited, .sidebar a:hover, .sidebar a:active { text-decoration: none !important; color: inherit; }

.brand-bar { padding: 16px; border-bottom: 1px solid var(--border); display: flex; align-items: center; justify-content: space-between; flex-shrink: 0; }
.brand-name { font-size: 14px; font-weight: 600; color: var(--green); display: flex; align-items: center; gap: 8px; }
.school-picker { display: flex; align-items: center; gap: 10px; padding: 10px 16px; border-bottom: 1px solid var(--border); cursor: pointer; flex-shrink: 0; }
.school-picker:hover { background: var(--bg); }
.school-icon { width: 32px; height: 32px; background: var(--green-light); border-radius: 8px; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.school-icon i { font-size: 16px; color: var(--green); }
.school-info .name { font-size: 12px; font-weight: 600; color: var(--text); }
.school-info .sub  { font-size: 10px; color: var(--text-muted); }

.nav-group { padding: 6px 0; }
.nav-label { font-size: 10px; font-weight: 600; color: var(--text-hint); text-transform: uppercase; letter-spacing: .07em; padding: 6px 16px 2px; }
.nav-item { display: flex; align-items: center; gap: 9px; padding: 7px 16px; font-size: 12.5px; color: var(--text-muted); cursor: pointer; transition: background .12s; border-radius: 0; }
.nav-item i { font-size: 15px; flex-shrink: 0; }
.nav-item:hover { background: var(--bg); color: var(--text); }
.nav-item.active { background: var(--green-light); color: var(--green); font-weight: 600; }
.nav-sub .nav-item { padding: 5px 16px 5px 32px; font-size: 12px; }

/* Overrides and active states */
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

/* Highlight Nav Label if it has an active or open item */
.nav-group:has(.nav-item.active) .nav-label,
.nav-group:has(.nav-sub-container.open) .nav-label {
  color: var(--green) !important;
}
"""

# Replace the existing style block with the new comprehensive one
import re
new_content = re.sub(r'<style>.*?</style>', f'<style>\\n{full_sidebar_css}\\n</style>', content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_content)
    
print("Updated sidebar.html with full CSS!")
