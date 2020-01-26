"""
measure.py

Functions for measuring geometrical data in atom arrays

"""

import numpy as np

from .atom_data import atomic_weights

def calculate_distance(rA, rB):
    """
    Calculate the distance between two points.

    Parameters
    ----------
    rA, rB : np.ndarray
        The coordinates of each point.

    Returns
    -------
    distance : float
        The distance between the two points.

    Examples
    --------
    >>> r1 = np.array([0,0,0])
    >>> r2 = np.array([0,0.1,0])
    >>> calculate_distance(r1,r2)
    0.1

    """
    # This function calculates the distance between two points given as numpy arrays.

    if not isinstance(rA, np.ndarray)  or not isinstance(rB, np.ndarray):
        raise TypeError("Input must be type np.ndarray for calculate_distance!")


    distance_vector = (rA - rB)
    distance = np.linalg.norm(distance_vector)

    return distance


def calculate_angle(rA, rB, rC, degrees=False):
    """
    Calculate the angle between three points.

    Parameters
    ----------
    rA, rB, rC : np.nparray
        The coordinates of each point

    degrees : str, Optional, default=radians
        Units of angle calculated

    Returns
    -------
    theta : float
        The angle between the three points.
    """
    # Calculate the angle between three points. Answer is given in radians by default, but can be given in degrees
    # by setting degrees=True
    AB = rB - rA
    BC = rB - rC
    theta=np.arccos(np.dot(AB, BC)/(np.linalg.norm(AB)*np.linalg.norm(BC)))

    if degrees:
        return np.degrees(theta)
    else:
        return theta


def calculate_molecular_mass(symbols):
    """Calculate the mass of a molecule.

    Parameters
    ----------
    symbols : list
        A list of elements.

    Returns
    -------
    mass : float
        The mass of the molecule
    """
    molecular_mass = 0.0

    for atom in symbols:

        if atom not in atomic_weights.keys():
            raise ValueError(F"Element {atom} not supported.")

        molecular_mass += atomic_weights[atom]
       
    return molecular_mass


def calculate_center_of_mass(symbols, coordinates):
    """Calculate the center of mass of a molecule.

    The center of mass is weighted by each atom's weight.

    Parameters
    ----------
    symbols : list
        A list of elements for the molecule
    coordinates : np.ndarray
        The coordinates of the molecule.
 
    Returns
    -------
    center_of_mass: np.ndarray
        The center of mass of the molecule.
    Notes
    -----
    The center of mass is calculated with the formula
 
    .. math:: \\vec{R}=\\frac{1}{M} \\sum_{i=1}^{n} m_{i}\\vec{r_{}i}
 
    """
    total_mass = calculate_molecular_mass(symbols)

    mass_array = np.zeros([len(symbols),1])
    
    center_of_mass = sum(coordinates * mass_array) / total_mass

    for index in range(len(symbols)):
        mass_array[index] = atomic_weights[symbols[index]]

    center_of_mass = sum(coordinates * mass_array) / total_mass

#    x_coord = 0.0
#    y_coord = 0.0
#    z_coord = 0.0
#    atom_index = 0
#    while atom_index < symbols.shape[0]:
#        x_coord += atomic_weights[symbols[atom_index]] * coordinates[atom_index,0]
#        y_coord += atomic_weights[symbols[atom_index]] * coordinates[atom_index,1]
#        z_coord += atomic_weights[symbols[atom_index]] * coordinates[atom_index,2]
#        atom_index += 1
#
#    center_of_mass = np.array([x_coord/total_mass, y_coord/total_mass, z_coord/total_mass])

    return center_of_mass
