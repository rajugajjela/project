#!/bin/python3
def read_function(file):
    print("The file read from:",file)
    print(file.read())
    print()

def find_function(string):
    file=open("python_data.txt","r")
    if string in file.readline():
        print("string will be found:",string) 
        print()
        print("printing the founded string line:")
        for line in file:
            if string in line:
             print(line)  
    else:
         print("string does not exists ") 
 
 
      

file=open("python_data.txt","r")
word="on "
read_function(file)
find_function(word)
