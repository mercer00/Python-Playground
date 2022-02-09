x = open("text1_test.txt" , "r")
print(x.read())
x.close()

y = open("text2_test.txt" , "w+")
y_bytes = y.write("It's your birthday")
print(y_bytes)
print(y.read())
y.close()

try:
    z = open("text3_test.txt" , "w")
    z.write("Flow\nShow\nCars\nJewels\nFancy things")
finally:
    z.close()

with open("text3_test.txt" , "r") as f:
    print(f.readlines())

with open("text3_test.txt" , "r") as f:
    print(f.read().splitlines())

