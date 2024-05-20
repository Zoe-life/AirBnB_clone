#!/usr/bin/python3

"""
script that calculates the area of a rectangle

"""


def calculate_area(width, height):
    """
    Args:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.

    """

    if width <= 0 or height <= 0:
        raise ValueError

    return width * height


# Example usage
area = calculate_area(5, 4)
print(f"The area of the rectangle is: {area}")
