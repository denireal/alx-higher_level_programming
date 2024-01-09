#!/usr/bin/python3
"""
Module for the text_indentation function.
"""


def text_indentation(text):
    """
    Indents text based on specific punctuation marks (. ? :).

    Args:
        text (str): The input text string.

    Raises:
        TypeError: If text is not a string.

    Returns:
        None
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    indented_text = text[:]

    for punctuation_mark in ".?:":
        list_text = indented_text.split(punctuation_mark)
        indented_text = ""
        for sentence in list_text:
            sentence = sentence.strip(" ")
            indented_text = (
                sentence + punctuation_mark
                if indented_text == ""
                else indented_text + "\n\n" + sentence + punctuation_mark
            )

        print(indented_text[:-3], end="")
