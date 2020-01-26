"""
molecool
A python package for analysing and visualizing xyz files for MolSSI best practices workshop
"""

# Add imports here
from .functions import *
from .measure import calculate_angle, calculate_distance, calculate_molecular_mass, calculate_center_of_mass
from .molecule import build_bond_list
from .visualize import draw_bond_histogram, draw_molecule
from .atom_data import atom_colors, atomic_weights

import molecool.io

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
