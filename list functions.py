#list functions

list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [3,6,2,6,3,7,3,2,3,5,3,6,4,4,3,7]

list1.append(11)
print(list1)
list1.remove(11)
print(list1)
print(list2.count(3))
print(list1.index(1))
print(max(list1))
print(min(list1))
print(len(list1))
list1.reverse()
print(list1)