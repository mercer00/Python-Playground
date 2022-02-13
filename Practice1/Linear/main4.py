# tsa of cylinder = pi * r ** 2 * h + 2(pi * r ** 2)

from math import pi

radius = float(input("Radius of the cylinder: "))
height = float(input("Height of the cylinder: "))

area = round((pi * (radius ** 2)) * height + (2 * (pi * (radius ** 2))), 2)

print(f"The total surface area of the cylinder is: {area}")
