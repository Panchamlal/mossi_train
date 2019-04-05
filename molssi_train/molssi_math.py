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
    # Check that input is type list
    if not isinstance(num_list, list):
        raise TypeError('Invalid input {} - Input must be of type list'.format(str(num_list)))

    # check that list is not empty
    if len(num_list) == 0:
        raise ValueError('enetered list of numbers is empty')

    sum = 0.0
    for num in num_list:
        try:
            sum = num + sum
        except TypeError:
            raise('Cannot Calculate mean of list - all elements must be of type int/float')

    mean = sum / len(num_list)
    # print("The mean of list {} is {}".format(num_list, mean))

    return mean


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
