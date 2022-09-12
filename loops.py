#!/bin/bash

a=100
b=200
print("a:",a)
print("b:",b)
if a<b:
  print("a is less than b")
print("\n")

x=100
y=300
print("x:",x)
print("y:",y)
if x<y:
  print("x is less than y")
else:
 print("x is greater than y")
print("\n")

x=500
y=100
print("x:",x)
print("y:",y)
if x<y:
    print("x is less than y")
elif x>y:
    print("x is greater than y")
print("\n")

x=500
y=500
print("x:",x)
print("y:",y)
if x<y:
    print("x is less than y")
elif x==y:
    print("x is equal to y")
else :   
    print("x is greater than y")
print("\n")

x=100
y=200
print("x:",x)
print("y:",y)
if x<y or x>y:
    print("x is less than y") 
print("\n")

x=100
y=100
print("x:",x)
print("y:",y)
if x<y and x>y:
    print("x is less than y") 
else:
    print("x is equal to y")    
print("\n")

x = 50
if x > 10:
  print("x value is above 10")
  if x > 20:
    print("x is above 20")
  else:
    print("x is above 30")
print("\n")

a=1
while a<10:
    print("a:",a)
    a=a+1
print("\n")

print("break statement used in while loop")
a=10
while a<20:
    print(a)
    if a==15:
        break
    a=a+1
print("\n")

print("continue statement used in while loop")
a=10
while a<20:
    a=a+1
    if a==15:
        continue
    print(a)
print("\n")


print("while loop using list:")
print("printing sets before loop")
list=['raju','nani','siddu','ammu']
print(list)
print("printing list after loop")
i=0
while i<len(list):
    print(list[i])
    i=i+1
print("\n")

print("while loop using sets:")
print("printing sets before loop")
sets=('1','2','3','4')
print(sets)
print("printing sets after loop")
i=0
while i<len(sets):
    print(sets[i])
    i=i+1
print("\n")

print("while loop using tuples:")
print("printing sets before loop")
tuple=('raju','nani','siddu','ammu')
print(tuple)
print("printing tuple after loop")
i=0
while i<len(tuple):
    print(tuple[i])
    i=i+1
print("\n")


print("for loop using tuples:")
tuple = ("A", "B", "C","D","E")
for x in tuple:
  print(x)
print("\n")

print("for loop using sets:")
print("printing sets before loop")
sets={'raju','nani','siddu','ammu'}
print(sets)
print("printing sets after loop")
for x in sets :
     print(x)
print("\n")

print("for loop using list:")
print("printing sets before loop")
list=['raju','nani','siddu','ammu']
print(list)
print("printing list after loop")
for x in list :
     print(x)
print("\n")