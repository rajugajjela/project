# from xml.dom import minidom
# dat=minidom.parse("task.xml")
# tagname= dat.getElementsByTagName("list")
# print(tagname)

# tagname= dat.getElementsByTagName('list')
# print(tagname[0].attributes['commitText'].value)
import xml.dom.minidom
  
docs = xml.dom.minidom.parse("task.xml")
  
print(docs.nodeName)
print(docs.firstChild.tagName)