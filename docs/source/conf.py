import os
import sys

import sphinx_rtd_theme
import distutils.util

extensions = [
    "sphinx_rtd_theme",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx.ext.mathjax",
    "sphinx.ext.autosectionlabel",
    "nbsphinx",
    "sphinx_gallery.load_style",
]

autosectionlabel_prefix_document = True


intersphinx_mapping = {
    'pysam': ('http://pysam.readthedocs.org/en/latest', None),
    'numpy': ('http://numpy.readthedocs.org/en/latest', None),
}


sys.path.insert(0, os.path.abspath('../..'))

project = 'footprint-tools'
copyright = '2020, Jeff Vierstra'
author = 'Jeff Vierstra'
release = '1.1.5'
templates_path = ['_templates']
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}
master_doc = 'index'
pygments_style = 'sphinx'
html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']
html_css_files = ['extra.css']


# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
_libdir = "../../build/lib.%s-%s.%s" % (distutils.util.get_platform(),
                                        sys.version_info[0], sys.version_info[1])

if os.path.exists(_libdir):
    sys.path.insert(0, os.path.abspath(_libdir))


mathjax_path="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"
