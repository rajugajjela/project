#!/bin/python3

file = open("python.txt", "w")
file.write("Hi this is a python script\n"
            "I work on functions\n"
            "I work onto files")

file = open("python.txt", "r")
print(file.read())
# print(file)

file = open("python.txt", "r")
file1 = open("new.txt", "w")
for line in file:
    file1.write(line)

