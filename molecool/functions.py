"""
functions.py
A python package for analysing and visualizing xyz files for MolSSI best practices workshop

Handles the primary functions
"""


def canvas(with_attribution=True):
    """
    Placeholder function to show example docstring (NumPy format)

    Replace this function and doc string for your own project

    Parameters
    ----------
    with_attribution : bool, Optional, default: True
        Set whether or not to display who the quote is from

    Returns
    -------
    quote : str
        Compiled string including quote and optional attribution
    """

    quote = "This package isn't just cool, it's MOLEcool!!!"
    if with_attribution:
        quote += "\n\t- Adapted from Not Henry David Thoreau"
    return quote


if __name__ == "__main__":
    # Do something if this file is invoked on its own
    print(canvas())
