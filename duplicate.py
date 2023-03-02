#!/bin/python

lines_seen=set()
outfile = open("out.txt", "w")
for line in open("1.txt", "r"):
    if line not in lines_seen:
        outfile.write(line)
        lines_seen.add(line)
outfile.close()

