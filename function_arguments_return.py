# Import the math module to access mathematical constants and functions
import math

# Define the function to calculate the area of a circle
def circle_area(radius):
    """
    Calculate and return the area of a circle given its radius.
    
    Parameters:
    radius (float): The radius of the circle.
    
    Returns:
    float: The area of the circle.
    """
    # Calculate the area using the formula: area = π * radius^2
    area = math.pi * (radius ** 2)
    
    # Return the calculated area
    return area

# Define the radius value to be used in the calculation
radius_value = 5

# Call the circle_area function with the radius_value and store the result
area_result = circle_area(radius_value)

# Display the result using an f-string with two decimal places
print(f"The area of a circle with radius {radius_value} is: {area_result:.2f}")
