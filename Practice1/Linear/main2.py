from random import randint

number = randint(100, 999)

strNum = str(number)
sum = 0

for i in strNum:
    sum += int(i)
print(number)
print(sum)
