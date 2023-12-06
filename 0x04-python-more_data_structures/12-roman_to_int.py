#!/usr/bin/python3


def roman_to_int(roman_string):
    """
    Function to convert a Roman numeral string to an integer.

    Parameters:
    - roman_string (str): The input Roman numeral string.

    Returns:
    - int: The integer equivalent of the Roman numeral. Returns 0 if the
    input is not a non-empty string.
    """
    # Check if the input is a non-empty string
    if type(roman_string) != str or not roman_string:
        return 0

    # Dictionary mapping Roman numerals to their integer values
    r_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    # Variables to keep track of the current and previous Roman numeral values
    current_value = 0
    previous_value = 0

    # Variable to store the total integer value
    roman_integer = 0

    # Iterate through each character in the Roman numeral string
    for i in range(len(roman_string)):
        # Get the integer value of the current Roman numeral
        current_value = r_dict[roman_string[i]]

        # Check if the current value is greater than the previous value
        if current_value > previous_value:
            # Subtract 2x the previous value to correct for d double counting
            roman_integer = roman_integer + current_value - 2 * previous_value
        else:
            # Add the current value to the total
            roman_integer = roman_integer + current_value

        # Update the previous value for the next iteration
        previous_value = current_value

    # Return the final total
    return roman_integer
