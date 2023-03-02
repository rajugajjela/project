#!/bin/python3
file=open("python_data.txt", "r")
for line in file:
 length=len(line.split())
 if length == 4:
        print("words in a line:",length)
        print(line)   
