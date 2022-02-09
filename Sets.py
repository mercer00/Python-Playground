set1 = {0,1,2,3,4,5,6,7,8,9}
print(set1)
set1.remove(0)
set1.add(10)
print(set1)

set2 = {1,2,3,4,5,6}
set3 = {4,5,6,7,8,9}

print(set2 | set3)
print(set2 & set3)
print(set2 - set3)
print(set3 - set2)
print(set2 ^ set3)