#!/usr/bin/python3

"""
script that calculates the area of a rectangle

"""


def calculate_area(width, height):
    """
    Calculates the area of a rectangle.

    Args:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.

    Returns:
        float: The calculated area of the rectangle.

    Raises:
        ValueError: If either width or height is non-positive.
    """

    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be positive numbers.")

    return width * height


# Example usage
area = calculate_area(5, 4)
print(f"The area of the rectangle is: {area}")
