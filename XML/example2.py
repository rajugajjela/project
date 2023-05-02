# Using fromstring() function:
import xml.etree.ElementTree as ET
data='''<?xml version="1.0" encoding="UTF-8"?>
<metadata>
<food>
    <item name="breakfast">Idly</item>
    <price>$2.5</price>
    <description>
   Two idly's with chutney
   </description>
    <calories>553</calories>
</food>
</metadata>
'''
# Finding Elements of Interest:
myroot = ET.fromstring(data)
print(myroot)
print("\n")

print(myroot.tag)
print("\n")

print(myroot.tag[0:4])
print("\n")

print(myroot.attrib)
print("\n")

print(myroot[0].tag)
print("\n")

for x in myroot[0]:
     print(x.tag, x.attrib)
print("\n")

for x in myroot[0]:
        print(x.text)
print("\n")       


print("\n")       

