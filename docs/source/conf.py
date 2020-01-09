project = "VG Ansible Collection"
copyright = "2020"
author = "Vladimir Gurinovich"

extensions = [
    "sphinx_rtd_theme",
]
exclude_patterns = []

html_theme = "sphinx_rtd_theme"
html_context = {
    "display_github": True,
    "github_user": "gurv",
    "github_repo": "vg-ansible",
    "github_version": "master",
    "conf_py_path": "/docs/source/",
}
