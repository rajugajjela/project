#!/bin/python


print("join the tuples:")
print("before join the tuples:")
tuples1=('raju','nani','siddu','ammu')

tuples2=('1','2','3','5','4')

tuples3=tuples1+tuples2

print("Type of tuples:",type(tuples1))
print("tuples1:",tuples1)
print("tuples2:",tuples2)

print("after join the tuples")
print("tuples3:",tuples3)
print("\n")


print("inserting operation by using tuples")

tuple1= ('a', 'b', 'c', 'd', 'f')
print("brefore inserting to the tuple:",tuple1)
x=list(tuple1)
x.insert(4, 'e')
x=tuple(x)

print('tuple after inserting:',x)
print("\n")


print("extend operation by using tuples:")
tuple1 = (2, 3, 5)

tuple2 = (1, 4, 7)
print("before extend tuple1:",tuple1)
print("before extend tuple2:",tuple2)

x=list(tuple1)
y=list(tuple2)

x.extend(y)
x=tuple(x)
print('tuples after extend:',x)
print("\n")


print("append operation using tuples:")

tuples =('raju', 'nani','sravs')

print("before append:",tuples)
x=list(tuples)

x.append('rani')
x=tuple(x)
print("after append:",x)
print("\n")


print("pop operation in tuples:")
tuples1=('raju','nani','siddu','ammu')

tuples2=('1','2','3','5','4')

print("before pop operation")
print("tuples1:",tuples1)
print("tuples2:",tuples2)

x=list(tuples1)
y=list(tuples2)
print("after pop operation")
x.pop(0)
x=tuple(x)
print("tuples1:",x)

y.pop(3)
y=tuple(y)
print("tuples2:",y)
print("\n")


print("remove operation in tuples:")
tuples1=('raju','nani','siddu','ammu')
tuples2=('1','2','3','5','4')

print("before remove operation")
print("tuples1:",tuples1)
print("tuples2:",tuples2)

x=list(tuples1)
y=list(tuples2)
print("after remove operation")
x.remove('siddu')
x=tuple(x)
print(x)

y.remove('5')
y=tuple(y)
print(y)
print("\n")


print("reverse operation in tuples:")
tuples1=('Aa','Ee','Ff','Dd','Bb','Cc')

tuples2=('1','3','4','2','6','5')

print("before reverse operation")
print("tuples1:",tuples1)
print("tuples2:",tuples2)

print("after reverse operation")

x=list(tuples1)
y=list(tuples2)
x.reverse()
x=tuple(x)
print(x)

y.reverse()
y=tuple(y)
print(y)
print("\n")

print("sort operation in tuples:")
tuples1=('Aa','Ee','Ff','Dd','Bb','Cc')

tuples2=('1','3','4','2','6','5')

print("before sort operation")
print("tuples1:",tuples1)
print("tuples2:",tuples2)

print("after sort operation")

x=list(tuples1)
y=list(tuples2)
x.sort()
x=tuple(x)
print(x)

y.sort()
y=tuple(y)
print(y)
print("\n")


print("sort.lower operation in tuples:")
tuples1=('skd','ksmd','dij','2','Dd','1','B','4','dj','3')

tuples2=('1','3','4','2','6','5')

print("before sort.lower operation")
print("tuples1:",tuples1)
print("tuples2:",tuples2)

print("after sort.lower operation")

x=list(tuples1)
x.sort(key=str.lower)
x=tuple(x)
print(x)

y=list(tuples2)
y.sort(key=str.lower)
y=tuple(y)
print(y)
print("\n")

print("for loop using tuples:")
tuple = ("A", "B", "C","D","E")
for x in tuple:
  print(x)
print("\n")


print("while loop using tuples:")
tuple = ("1", "2", "3","4","5","6","7","8","9")
i = 0
while i < len(tuple):
  print(tuple[i])
  i = i + 1
print("\n")

print("count operations using tuples")
tuple = (1, 3,4, 7,4, 8, 7,4 ,5, 4, 6, 8, 5)

x = tuple.count(4)

print(x)
print("\n")

 
print("printing the index number in tuples")
tuple = (1,2,3,5,4,3,5,9,7,5,3,2)

x = tuple.index(4)

print(x)
print("\n")

print("checking if condition in tuples")
fruits = ("apple", "banana", "grapes", "kiwi")

if "apple" in fruits:
  print("Yes, 'apple' is in the fruits tuple")
else:
    print("apple is not in fruit tuple")