"""
pdb.py

Functions for I/O with pdb file format
"""

import numpy as np

def open_pdb(file_loc):
    """
    Open and read coordinates and symbols from a pdb file.

    The pdb file must specify the atom elements in the last column, and follow the conventions outlined in the PDB format specification.

    Parameters
    ----------
    file_location : str
        The location of the pdb file to be read in

    Returns
    -------
    symbols : list 
        The atomic symbols from the pdb file
    coordinates : np.ndarray
        The atomic coordinates from the pdb file

    """
    # This function reads in a pdb file and returns the atom names and coordinates.
    with open(file_loc) as f:
        data = f.readlines()

    coordinates = []
    symbols = []
    for line in data:
        if 'ATOM' in line[0:6] or 'HETATM' in line[0:6]:
            symbols.append(line[76:79].strip())
            atom_coordinates = [float(x) for x in line[30:55].split()]
            coordinates.append(atom_coordinates)

    # Convert list to numpy array
    coordinates = np.array(coordinates)

    return symbols, coordinates

