import random

intRange = input("Integer range(ex, 1-10): ").split("-")
intStart = int(intRange[0])
intEnd = int(intRange[1])
randomInt = random.randint(intStart, intEnd)

floatRange = input("Float range(ex, 1.5-1.9): ").split("-")
floatStart = float(floatRange[0])
floatEnd = float(floatRange[1])
randomFloat = round(random.uniform(floatStart, floatEnd), 2)

print(f"Random integer: {randomInt}")
print(f"Random float {randomFloat}")
