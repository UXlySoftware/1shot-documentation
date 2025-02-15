# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = '1Shot API'
copyright = '2025, UXly Software'
author = 'UXly Software'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.githubpages'
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'alabaster'
html_title = '1Shot Docs'
#html_logo = '' # https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_logo
#html_favicon = '' # https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_favicon
html_show_sphinx = False
html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_baseurl = 'https://docs.1shotapi.com'
