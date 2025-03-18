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
    'sphinx.ext.githubpages',
    'sphinx_design',
    'sphinx_copybutton'
]

templates_path = ['_templates']
exclude_patterns = []

# -- Sphinx-copybutton options ---------------------------------------------
# Exclude copy button from appearing over notebook cell numbers by using :not()
# The default copybutton selector is `div.highlight pre`
# https://github.com/executablebooks/sphinx-copybutton/blob/master/sphinx_copybutton/__init__.py#L82
copybutton_exclude = ".linenos, .gp"
copybutton_selector = ":not(.prompt) > div.highlight pre"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'alabaster'
html_title = '1Shot Docs'
html_logo = '_static/1shot-logo.svg' # https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_logo
html_favicon = '_static/favicon.ico' # https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_favicon
html_show_sphinx = False
html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_baseurl = 'https://docs.1shotapi.com'
html_theme_options = {
    "icon_links": [
        {
            # Label for this link
            "name": "GitHub",
            # URL where the link will redirect
            "url": "https://github.com/uxlySoftware/1shot-documentation",  # required
            # Icon class (if "type": "fontawesome"), or path to local image (if "type": "local")
            "icon": "fa-brands fa-github",
            # The type of image to be used (see below for details)
            "type": "fontawesome",
        },
        {
            # Label for this link
            "name": "X",
            # URL where the link will redirect
            "url": "https://x.com/uxlysoftware",  # required
            # Icon class (if "type": "fontawesome"), or path to local image (if "type": "local")
            "icon": "fa-brands fa-x-twitter",
            # The type of image to be used (see below for details)
            "type": "fontawesome",
        },
        {
            # Label for this link
            "name": "Discord",
            # URL where the link will redirect
            "url": "https://discord.gg/xkF9NFS6",  # required
            # Icon class (if "type": "fontawesome"), or path to local image (if "type": "local")
            "icon": "fa-brands fa-discord",
            # The type of image to be used (see below for details)
            "type": "fontawesome",
        }
   ],
   "secondary_sidebar_items": ["page-toc"],
}
