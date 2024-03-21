"""
This module provides functions to
determine the type of a triangle based on its side.

Functions:
- triangle_type(side1, side2, side3):
    Determines the type of triangle based on the lengths of its sides.
- main():
    Prompts the user to input the lengths of the sides of a triangle and
                                           prints out the type of triangle.

Example:
  To determine the type of a triange, you can use the 'triangle_type' function:
  >>> triangle_type(3,3,3)
  'Equilateral'

  Alternatively, you can run the 'main' function,
             which prompts the user for input:
  >>> main()
  Enter the length of side 1: 3
  Enter the length of side 2: 4
  Enter the length of side 3: 5
  The triangle is Scalene
"""


def triangle_type(side1, side2, side3):
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"


def main():
    side1 = int(input("Enter the length of side 1: "))
    side2 = int(input("Enter the length of side 2: "))
    side3 = int(input("Enter the length of side 3: "))

    triangle = triangle_type(side1, side2, side3)
    print("The triangle is", triangle)


if __name__ == "__main__":
    main()
