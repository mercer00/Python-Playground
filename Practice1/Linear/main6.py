# ord(value) , ord takes a character as its value and returns its unicode value
# chr(value) , vhr takes a unicode value as its value and returns a character

letter = input("Letter(a-z): ")
letterA = ord("a")
if letter == "a":
    print(1)
else:
    letterUni = ord(letter)
    print(letterUni - letterA + 1)
