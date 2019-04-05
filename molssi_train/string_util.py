"""
string_util.py
This is the project for molssi training.

Some string processing functions

"""

def title_case(sentence):
    """
    Converts enetered string into the title_case

    Parameters
    -----------
    sentence : string
        string to be converted into sentence case

    Returns
    -------
    title_case_sentence : string
        string in TITLE CASE

    Example
    -------
    >>>title_case('ThiS iS a StRING')
        This Is A String.

    >>>
    """
    title_case_sentence = ""
    list_of_word = sentence.split(' ')

    for words in list_of_word:
        words = words[0].upper() + words[1:].lower()
        title_case_sentence =  title_case_sentence + " " + words

    return title_case_sentence
