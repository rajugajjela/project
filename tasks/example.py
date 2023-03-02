with open("change.xml") as fp: 
	content=fp.read()
from nis import match
import re
# regex =r"a.*b|\d+" 
fp=open("change.xml","r")
for line in fp:
    if "commit " in line:
       match = re.findall(r'(?:\d+[a-zA-Z]+|[a-zA-Z]+\d+)+',line)
print(match)