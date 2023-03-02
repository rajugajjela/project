import xml.etree.ElementTree as ET
my_file = ET.parse('commits_table.xml')
a='Commit Text'
b="commits"
# html_body=('<BODY> <table border=1><tr> <td>Commit Text</td><td>commits</td></tr>')
f = open('my_file_zip.html','w')
c=f.write(a)
d=f.write(b)

for x in my_file.findall('hudson.plugins.repo.ChangeLogEntry'):
     commit_text=x.find('commitText').text
     commits=x.find('revision').text
#     # print("commitText is:",commit_text)
#     # print("commit is:",commits)
#     print("\n")
     e=f.write(commit_text)
     g=f.write(commits)
r=zip(c,d,e,g)
print(tuple(r))



