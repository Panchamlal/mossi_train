"""
molssi_math.py
This is the project for molssi training.

Some math functions
"""


def mean(num_list):
    """
    Calculate the mean/average of a list of numbers

    Parameters
    -----------
    num_list: The list of number

    Returns
    -------
    mean : float
    """
    sum = 0.0
    for num in num_list:
        sum = num + sum

    mean = sum / len(num_list)
    print("The mean of list {} is {}".format(num_list, mean))

    return None


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

    quote = "The code is but a canvas to our imagination."
    if with_attribution:
        quote += "\n\t- Adapted from Henry David Thoreau"
    return quote


if __name__ == "__main__":
    # Do something if this file is invoked on its own
    print(canvas())
