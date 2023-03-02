import re
import xml.etree.ElementTree as ET

def file_split(data):
    print("Splitting the file:",data)
    variable = 'sub-log'
    my_file = ET.parse(data)
    char = "a"
    for x in my_file.findall(variable):
    
        with open('New_file_' + char + '.xml', 'wb') as f:
            ET.ElementTree(x).write(f)
            i = ord(char)
            i += 1
            char = chr(i)
    print("Splitting the file was completed.")   
    print("\n")     


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
     data = data.replace("  ","")
     data = data.replace("\n\n","\n")
     data = data.replace("\n     \n","\n")
     data = data.replace('<sub-log scm="git https://dummy/_git/Application">'," ")
     data = data.replace('<sub-log scm="git https://dummy/_git/MApp">'," ")
     data=data.strip()
  
    with open( file_data, 'w') as file:
     file.write(data)

    print("Replacing the file was completed") 
    print("\n")     

def table_func(data):
    print("converting to HTML table")
    variable='hudson.plugins.repo.ChangeLogEntry'
    my_file = ET.parse(data)
    html_body=('<BODY> <table border=1><tr> <td>Commit Text</td><td>commits</td></tr>')
    f = open('commits.html','w')
    f.write(html_body)

    for x in my_file.findall(variable):
      commit_text=x.find('commitText').text
      commits=x.find('revision').text
      print(commit_text)
      print(commits)
      f.write('<tr><td>%s</td>  <td>%s</td> </tr>'%(commit_text,commits))
    print("converting to HTML table was completed succsesfully")
    print("\n") 

def table_func_2(data):
    word_2 ='committer'
    word_1 = 'commit '
    file = open(data, "r")
    FILE=open('commits.html','a')
    for x in file:     
            if re.search(word_1, x): 
               line=x[7:]
               print(line)
            if re.search(word_2,x):
                a=next(file)
                new=a
                print(new)
                FILE.write('<tr><td>%s</td>  <td>%s</td> </tr>'%(line,new))




file_split("changelog_test.xml")
file_replace("New_file_a.xml")
file_replace("New_file_b.xml")
file_replace("New_file_c.xml")
table_func("New_file_a.xml")
table_func_2("New_file_b.xml")
table_func_2("New_file_c.xml")
