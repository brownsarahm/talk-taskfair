# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Intro to ML for Scientists'
copyright = '2023, Sarah M Brown'
author = 'Sarah M Brown'

# The short X.Y version
version = '2023.04.04'

# The full version, including alpha/beta/rc tags
release = '2023.04.04'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_nb",
    'sphinx.ext.intersphinx',
    "sphinx_panels",
    "sphinxcontrib.bibtex",
    'hieroglyph',
    'sphinxcontrib.mermaid'
]

# "ablog",
# "sphinxext.opengraph",

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates', '_build', 'Thumbs.db', '.DS_Store', "*import_posts*",
        "**/pandoc_ipynb/inputs/*", "README.md", '_bibliography',
        '_data','_pages','_people','_projects']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_book_theme'
# 'pydata_sphinx_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_theme_options = {
  "github_url": "https://github.com/brownsarahm/",
  "twitter_url": "https://twitter.com/brownsarahm",
  "search_bar_text": "Search this site...",
  "google_analytics_id": "",
  "navbar_end": ["search-field.html", "navbar-icon-links"],
}

# -- Extension configuration -------------------------------------------------


# Panels config
panels_add_bootstrap_css = False

# MyST config
myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    # "fieldlist",
    "html_admonition",
    "html_image",
    # "linkify",
    "replacements",
    "smartquotes",
    # "strikethrough",
    "substitution",
    "tasklist",
]

# Bibliography and citations
bibtex_bibfiles = ["_static/references.bib"]


nb_render_priority = {
  "html": (
            "application/vnd.jupyter.widget-view+json",
            "application/javascript",
            "text/html",
            "image/svg+xml",
            "image/png",
            "image/jpeg",
            "text/markdown",
            "text/latex",
            "text/plain",
        ),
  "slides": (
            "application/vnd.jupyter.widget-view+json",
            "application/javascript",
            "text/html",
            "image/svg+xml",
            "image/png",
            "image/jpeg",
            "text/markdown",
            "text/latex",
            "text/plain",
        ),
  "revealjs": (
            "application/vnd.jupyter.widget-view+json",
            "application/javascript",
            "text/html",
            "image/svg+xml",
            "image/png",
            "image/jpeg",
            "text/markdown",
            "text/latex",
            "text/plain",
        )
}


#  --------------Slides

slide_theme = 'slides'

slide_theme_options = {
    'presenters': [
        {
            'name': 'Sarah M Brown',
            'twitter': '@brownsarahm',
            'www': 'http://sarahmbrown.org',
            'github': 'http://github.com/brownsarahm/'
        },
    ],
    'custom_css': 'custom.css'}

slide_numbers = True
# slide_footer = 'Integrating Ethics into Data Science Courses- Sarah M Brown'

def setup(app):
    app.add_css_file('_static/custom.css')
