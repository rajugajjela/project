import xml.etree.ElementTree as ET
my_file = ET.parse('commits_table.xml')
html_body=('<BODY> <table border=1><tr> <td>Commit Text</td><td>commits</td></tr>')
f = open('commits_table.html','w')
f.write(html_body)

for x in my_file.findall('hudson.plugins.repo.ChangeLogEntry'):
    commit_text=x.find('commitText').text
    commits=x.find('revision').text
    # print("commitText is:",commit_text)
    # print("commit is:",commits)
    print("\n")
    f.write('<tr><td>%s</td>  <td>%s</td> </tr>'%(commit_text,commits))




