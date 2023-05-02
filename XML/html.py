import re
import xml.etree.ElementTree as ET
from itertools import islice

def file_replace(file_data):
    print("Replacing the file:",file_data)
    with open( file_data, 'r') as file:
     data = file.read()
     data = data.replace("&lt;", "<")
     data = data.replace("&gt;", ">")
     data = data.replace('<sub-log scm="repo ssh://dummy/manifest.git default.xml manifest">'," ")
     data = data.replace("&amp;quot;","" "")
     data = data.replace("<multi-scm-log>"," ")
     data = data.replace("</multi-scm-log>"," ")
     data = data.replace("</sub-log>"," ")
     data = data.replace("&apos;","'")
     data = data.replace("&quot;","'")
    #  data = data.replace("\n"," ")
    #  data = data.replace("  ","\n")
    #  data = data.replace("\n     \n","")
     data = data.replace('<sub-log scm="git https://dummy/_git/Application">'," ")
     data = data.replace('<sub-log scm="git https://dummy/_git/MApp">'," ")
     data=data.strip('\n\n')
  
    with open( file_data, 'w') as file:
     file.write(data)

def remove_empty(data):
    with open(data,'r+') as fd:
        lines = fd.readlines()
        fd.seek(0)
        fd.writelines(line for line in lines if line.strip())
        fd.truncate()


def new(data):
    print("converting to HTML table")
    variable='hudson.plugins.repo.ChangeLogEntry'
    my_file = ET.parse(data)
    html_body=('<BODY> <table border=1><tr> <td>Commit Text</td><td>commits</td></tr>')
    f = open('my_html.html','w')
    f.write(html_body)

    for x in my_file.findall(variable):
      commit_text=x.find('commitText').text
      commits=x.find('revision').text
      print(commit_text)
      print(commits)
      f.write('<tr><td>%s</td>  <td>%s</td> </tr>'%(commit_text,commits))





def table_func_2(data):
    with open(data,'r'):
        pattern = "committer"
        var = "commit "
        file = open(data, "r")
        FILE = open('my_html.html','a')
        for x in file:    
            if re.search(pattern, x):         
                print(next(file))
            if  re.search(var,x):
                print(x)
            # FILE.write('<tr><td>%s</td><td>%s</td></tr>'%(h,x))



file_replace("New_file_b.xml")
remove_empty("New_file_b.xml")
remove_empty("New_file_a.xml")
new("New_file_a.xml")
table_func_2("New_file_b.xml")
