#While loop that tells whether a number is odd or even

x = 0
while x < 11:
    if x%2 == 0:
        print(f"{x} is an even number")
    else:
        print(f"{x} is an odd number")
    x += 1
    