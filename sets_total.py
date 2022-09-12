#!/bin/python

print("printing sets before operation")
sets={'raju','nani','siddu','ammu'}
print("length of sets:",len(sets))
print("Type of sets:",type(sets))
print(sets)
for x in sets :
     print(x)
print("\n")

print("add operation in sets")
sets={'raju','nani','siddu','ammu'}

print("before add operation:")
print(sets)
sets.update("soumya")
print("after add operation:")
print(sets)
print("\n")


print("update operation in sets")
print("before update operation:")
sets={'1','2','3','5','4'}
print(sets)
print("after update operation:")
sets.update("7")
print(sets)
print("\n")


print("remove operation in sets")
sets={'raju','nani','siddu','ammu'}
print("before remove operation:")
print(sets)
sets.remove("siddu")
print("after remove operation:")
print(sets)
print("\n")

print("discard operation in sets")
sets={'raju','nani','siddu','ammu'}
print("before discard operation:")
print(sets)
sets.remove("nani")
print("after discard operation:")
print(sets)
print("\n")

print("pop operation in sets")
sets={'raju','nani','siddu','ammu'}
print("before pop operation:")
print(sets)
sets.pop()
print("after pop operation:")
print(sets)
print("\n")

print("clear operation in sets")
sets={'raju','nani','siddu','ammu'}
print("before clear operation:")
print(sets)
sets.clear()
print("after clear operation:")
print(sets)
print("\n")

print("join operation in sets")
set1={'raju','nani','siddu','ammu'}
set2={'1','2','3','5','4'}
print("before join operation:")
print(set1)
print(set2)
set3=set1.union(set2)
print("after join operation:")
print(set3)
print("\n")

print("join operation in sets")
set1={'raju','nani','siddu','ammu'}
set2={'1','2','3','5','4'}
print("before join operation:")
print(set1)
print(set2)
set3=set1.union(set2)
print("after join operation:")
print(set3)
print("\n")

print("update operation in sets")
set1={'raju','nani','siddu','ammu'}
set2={'1','2','3','5','4'}
print("before update operation:")
print(set1)
print(set2)
set1.update(set2)
print("after update operation:")
print(set1)
print("\n")

print("intersection_update operation in sets")
set1={'raju','nani','siddu','ammu'}
set2={'vamshi','sai','raju','anil'}
print("before intersection_update operation:")
print(set1)
print(set2)
set1.intersection_update(set2)
print("after intersection_update operation:")
print(set1)
print("\n")

print("symmetric_difference_update operation in sets")
set1={'raju','nani','siddu','ammu'}
set2={'vamshi','sai','raju','anil'}
print("before symmetric_difference_update operation:")
print(set1)
print(set2)
set1.symmetric_difference_update(set2)
print("after symmetric_difference_update operation:")
print(set1)
print("\n")
