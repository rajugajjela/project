# Parsing XML
import xml.etree.ElementTree as ET
tree = ET.parse('country_details.xml')
root = tree.getroot()
print(root)

print(root.tag)
print(root.attrib)

for child in root:
     print(child.tag, child.attrib)
print("\n")

print(root[0][1].text)
print(root[1][1].text)
print("\n")

for neighbor in root.iter('neighbor'):
       print(neighbor.attrib)
print("\n")

# Finding interesting elements
for country in root.findall('country'):
     rank = country.find('rank').text
     name = country.get('name')
     print(name, rank)
print("\n")

# // Modifying an XML File
for rank in root.iter('rank'):
     new_rank = int(rank.text) + 1
     rank.text = str(new_rank)
     rank.set('updated', 'yes')

tree.write('output_country.xml')

# Building XML documents
a = ET.Element('a')
b = ET.SubElement(a, 'b')
c = ET.SubElement(a, 'c')
d = ET.SubElement(c, 'd')
ET.dump(a)
