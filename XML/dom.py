from xml.dom import minidom
p1 = minidom.parse("simple.xml");
print(p1)

dat=open('simple.xml')
p2=minidom.parse(dat)
print(p2)

dat=minidom.parse('simple.xml')
print(dat)

tagname= dat.getElementsByTagName('item')[0]
print(tagname)

dat = minidom.parse('simple.xml')
tagname= dat.getElementsByTagName('item')
print(tagname[0].attributes['name'].value)

print(tagname[1].firstChild.data)

# print(items[1].attributes['name'].value)

# for x in item:
#     print(x.firstChild.data)

# print(len(items))