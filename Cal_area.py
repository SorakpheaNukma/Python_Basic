import math


def calculate_circle_area(radius):
    """
    Calculate the area of a circle based on its radius.

    Parameters:
    - radius (float): The radius of the circle.

    Returns:
    - float: The area of the circle.
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative.")

    area = math.pi * radius ** 2
    return area


# Example of using the function
circle_radius = 5.0
circle_area = calculate_circle_area(circle_radius)
print(f"The area of a circle with radius {circle_radius} is {circle_area:.2f}")