import os
import sys
from datetime import datetime

# -- Project information -----------------------------------------------------
project = 'BTick'
copyright = f'{datetime.now().year}, Sherif Fathey'
author = 'Sherif Fathey'
release = '1.0.0'
version = '1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo',
    'sphinx.ext.githubpages',
    'sphinx_rtd_theme',
    'sphinx_copybutton',
    "sphinx_design",
]

templates_path = ['_templates']
exclude_patterns = []

# Syntax highlighting
pygments_style = 'sphinx'
highlight_language = 'cpp'

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = '_static/logo.png'

html_theme_options = {
    'logo_only': False,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': True,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False,
}

# Add custom CSS
html_css_files = ['custom.css']

# Master doc
master_doc = 'index'

# Todo extension settings
todo_include_todos = True
