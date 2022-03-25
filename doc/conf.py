# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use the absolute path, like shown here.
import datetime
import sys
from pathlib import Path
sys.path.insert(0, str(Path('../').resolve()))


# -- Project information -----------------------------------------------------

project = 'NSIDC Git Training'
copyright = f'NSIDC {datetime.date.today().year}'
author = 'Matt Fisher, Marin Klinger'

# The full version, including alpha/beta/rc tags
release = 'v0.1.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
# NOTE: Order matters!
extensions = [
    # Parse Markdown:
    'myst_parser',
    # DRY out external links and reference them by name:
    'sphinx.ext.extlinks',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_notes', '_build', 'Thumbs.db', '.DS_Store', '_plugin']

# Suppress certain types of warnings.
# myst.header: "Non-consecutive header level increase"
suppress_warnings = ["myst.header"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']
html_static_path = []


# -- Options for LaTeX output --------------------------------------------------

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, document class
# [howto|manual], ???).
latex_documents = [(
    # Input file
    'index',
    # Output file
    'git-training.tex',
    # Title
    'NSIDC Git Training',
    # Authors
    author,
    'manual',
    False,
)]

latex_logo = './_images/nsidc-logo.svg'

latex_show_urls = 'footnote'

latex_show_pagerefs = True

latex_elements = {
    # remove blank pages
    'classoptions': ',openany,oneside',
    # Set pdf-wide table-of-contents depth
    'preamble': r'''
      \usepackage{hyperref}
      \setcounter{tocdepth}{3}
    '''
}


# -- Options for extlinks ------------------------------------------------------
extlinks = {
    'this_repo': (
        'https://bitbucket.org/nsidc/git-training',
        'git-training Bitbucket repository',
    ),
}
