#!/usr/bin/python3

"""UTF-8 Validator
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data: A list of integers representing 1-byte data.

    Returns:
        True if data is a valid UTF-8 encoding, else False.
    """
    num_bytes = 0

    for byte in data:
        if num_bytes == 0:
            # Check the number of bytes needed for the next character
            if byte >> 7 == 0b0:
                # Single-byte character
                num_bytes = 0
            elif byte >> 5 == 0b110:
                # Two-byte character
                num_bytes = 1
            elif byte >> 4 == 0b1110:
                # Three-byte character
                num_bytes = 2
            elif byte >> 3 == 0b11110:
                # Four-byte character
                num_bytes = 3
            else:
                # Invalid start byte
                return False
        else:
            # Check if byte is a continuation byte
            if byte >> 6 != 0b10:
                return False
            num_bytes -= 1

    # If num_bytes is not zero, then it's an incomplete character sequence
    return num_bytes == 0
