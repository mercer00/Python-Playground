#factorial

def factorial(x):
    if x == 1:
        return x
    else:
        return x * factorial(x-1)
 
print(factorial(5))

#using lambda

lambda_factorial = lambda x: 1 if x == 1 else x * lambda_factorial(x-1)

print(lambda_factorial(5))

#sequence
# 3,12,21,30,39

def sequence1(x):
    if x == 1:
        return 3
    else:
        return 9 + sequence1(x-1)

print(sequence1(3))
print(sequence1(10))

#same sequence using lambda

lambda_sequence1 = lambda x: 3 if x==1 else 9 + lambda_sequence1(x-1)

print(sequence1(3))
print(sequence1(10))


#recursions depending on each other

dependent_sequence = lambda x: 3 if x==1 else 9 + sequence1(x-1)

print(dependent_sequence(3))