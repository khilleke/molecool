"""
measure.py

Functions for measuring geometrical data in atom arrays

"""

import numpy as np

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
    for atom in symbols:
        molecular_mass += molecool.atom_data.atom_weights[atom]
       
    return molecular_mass
