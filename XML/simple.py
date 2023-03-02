# Using parse() function:
import xml.etree.ElementTree as ET
mytree = ET.parse('simple.xml')
myroot = mytree.getroot()
print(myroot)

# Finding Elements of Interest:
for x in myroot.findall('food'):
    item =x.find('item').text
    price = x.find('price').text
    calories = x.find('calories').text
    print(item, price,calories)
    
# # Modifying XML files:
# for description in myroot.iter('description'):
#      new_desc = str(description.text)+'wil be served'
#      description.text = str(new_desc)
#      description.set('updated', 'yes')
 
# mytree.write('new.xml')

# # Adding to XML:
# ET.SubElement(myroot[0], 'speciality')
# for x in myroot.iter('speciality'):
#      new_desc = 'South Indian Special'
#      x.text = str(new_desc)
 
# mytree.write('output_simple.html')

# # Deleting from XML:
# myroot[0][0].attrib.pop('name', None)
 
# # create a new XML file with the results
# mytree.write('output_simple2.xml')

# myroot[0].clear()
# mytree.write('output_simple3.xml')