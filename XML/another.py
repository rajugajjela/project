import xml.etree.ElementTree as ET
my_file = ET.parse('task.xml')
html_body="""<BODY>   <H4>Changes merged</H1><table border=1><tr></tr><tr> <td>Commit ID</td><td>commit Text</td></tr>"""
f = open('my_file2.html','w')
f.write(html_body)

for x in my_file.findall('hudson.plugins.repo.ChangeLogEntry'):
    commit_text=x.find('commitText').text
    commits=x.find('revision').text
    # print("commitText is:",commit_text)
    # print("commit is:",commits)
    print("\n")
    f.write('%s,%s'%(commit_text,commits))



