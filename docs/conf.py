# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'arbnb'
copyright = '2025, Andrés'
author = 'Andrés'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',        # Para docstrings estilo Google/NumPy (opcional)
    'sphinx_autodoc_typehints',  # Para que autodoc coja tipos de anotaciones (opcional)
]

import os
import sys
sys.path.insert(0, os.path.abspath('..'))  # Ajusta ruta al proyecto para que autodoc lo encuentre

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
