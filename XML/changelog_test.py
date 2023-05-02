import xml.etree.ElementTree as ET

variable = 'sub-log'
my_file = ET.parse('changelog_test.xml')
# root = my_file.getroot()
# print(root)
char = "a"
for x in my_file.findall(variable):
    
    with open('New_file_' + char + '.xml', 'wb') as f:
        ET.ElementTree(x).write(f)
        i = ord(char)
        i += 1
        char = chr(i)
        
