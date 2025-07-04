# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'DAPP_x-marsh_session'
copyright = '2025, christine schottmueller'
author = 'christine schottmueller'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
'nbsphinx', 'ipykernel', 'sphinx.ext.autodoc', 'sphinx.ext.mathjax'  
]

# enable latex and equation numbering in .rst
mathjax_path = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"

mathjax3_config = {
    "tex": {
        "tags": "all",  
        "useLabelIds": True
    }
}


templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'default'


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'alabaster'
# -- This will hide the project name next to the logo, showing only the image.
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'logo_only': True,
    'display_version': False,
}

html_static_path = ['_static']
# -- Link .css file that contains custom font
html_css_files = ['custom.css']

# -- Place logo in the top left corner of theme -----------------------------
html_logo = "_static/logo.png"


html_context = {
# Enable the "Edit in GitHub" link within the header of each page.
  'display_github': True,
  # Set the following variables to generate the resulting github URL for each page.
  'github_user': 'christineschottmueller',
  'github_repo': 'DAPP_x-marsh_session',
  'github_version': 'master/docs/'
}