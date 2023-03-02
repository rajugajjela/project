#!/bin/python

print("join the lists:")
print("before join the list:")
list1=['raju','nani','siddu','ammu']

list2=['1','2','3','5','4']

list3=list1+list2

print("Type of list:",type(list1))
print("Type of list:",type(list2))
print("list1:",list1)
print("list2:",list2)

print("after join the lists")
print("list3:",list3)
print("\n")


print("pop operation in list:")
list1=['raju','nani','siddu','ammu']

list2=['1','2','3','5','4']

print("before pop operation")
print("list1:",list1)
print("list2:",list2)

print("after pop operation")
list1.pop(0)
print("list1:",list1)

list2.pop(3)
print("list2:",list2)
print("\n")

print("remove operation in list:")
list1=['raju','nani','siddu','ammu']
list2=['1','2','3','5','4']

print("before remove operation")
print("list1:",list1)
print("list2:",list2)

print("after remove operation")
list1.remove('siddu')
print(list1)

list2.remove('5')
print(list2)
print("\n")

print("reverse operation in list:")
list1=['Aa','Ee','Ff','Dd','Bb','Cc']

list2=['1','3','4','2','6','5']

print("before reverse operation")
print("list1:",list1)
print("list2:",list2)

print("after reverse operation")

list1.reverse()
print(list1)

list2.reverse()
print(list2)
print("\n")

print("sort operation in lists:")
list1=['Aa','Ee','Ff','Dd','Bb','Cc']

list2=['1','3','4','2','6','5']

print("before sort operation")
print("list1:",list1)
print("list2:",list2)

print("after sort operation")

list1.sort()
print(list1)

list2.sort()
print(list2)
print("\n")


print("sort.lower operation in lists:")
list1=['skd','ksmd','dij','2','Dd','1','B','4','dj','3']

list2=['1','3','4','2','6','5']

print("before sort.lower operation")
print("list1:",list1)
print("list2:",list2)

print("after sort.lower operation")

list1.sort(key=str.lower)
print(list1)

list2.sort(key=str.lower)
print(list2)
