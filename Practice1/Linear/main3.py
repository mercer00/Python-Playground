from math import sqrt

height = float(input("Height of the Triangle: "))
base = float(input("Base of the Triangle: "))

# Area = 0.5 * base * height
# Perimeter = sum of all sides
# hypotenuse from pythagoras theorem

hypotenuse = round(sqrt(height ** 2 + base ** 2), 2)

area = round(0.5 * base * height, 2)
perimeter = round(height + base + hypotenuse, 2)

print(f"The Area is: {area}")
print(f"The perimeter is: {perimeter}")
