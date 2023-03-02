#!/bin/python3
import os
BUILDNUM = os.environ['BUILD_NUMBER']
print(BUILDNUM)
file = open("changelog.xml", "r")
for line in file:
    if "commit " in line:
         print(line[7:]) 
