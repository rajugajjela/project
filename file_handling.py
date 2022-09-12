#!/bin/bash

file = open("raj.txt", "r")
print(file.read())
print()

file = open("raj.txt", "r")
print(file.read(1))
print()

file = open("raj.txt", "r")
print(file.readlines())
print()

file = open("raj.txt", "r")
for x in file:
  print(x)

file = open("raj.txt", "r")
print(file.readlines())
file.close()
print()

file = open("raj.txt", "a")
file.write("I studied in sree chaitanya college of engineering.")
file.close()

file = open("raj.txt", "w")
file.write("I studied in sree chaitanya college of engineering.in karimnagar.")
file.close()

firstfile=open('nani.txt','r')  
secondfile=open('second.txt','w') 
#read content from first file
for line in firstfile:
               
 # write content to second file
 secondfile.write(line)