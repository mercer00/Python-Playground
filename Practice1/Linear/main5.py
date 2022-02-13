# circumference = 2 * pi * r
# area = pi * r ** 2
from math import pi

radius = float(input("The radius: "))

circumference = round(2 * pi * radius, 2)
area = round(pi * (radius ** 2), 2)

print(f"The circumference is: {circumference}")
print(f"The area is: {area}")
