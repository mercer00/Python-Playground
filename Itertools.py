import itertools

for i in itertools.count(5):
    print(i)
    if i == 10:
        break

for i in itertools.repeat("Shiva" , 3):
    print(i)

for i in itertools.cycle("Shiva"):
    print(i)
    if i == "a":
        break

print(list(itertools.accumulate(range(11))))
print(list(itertools.takewhile(lambda x: x <= 6 , list(range(0,11,2)))))
print(list(itertools.chain([1,2,3] , [4,5,6])))
list1 = ["A" , "B" , "C"]
print(list(itertools.product(list1 , [1 , 2])))
print(list(itertools.permutations(list1 , 2)))
print(list(itertools.permutations(list1)))

