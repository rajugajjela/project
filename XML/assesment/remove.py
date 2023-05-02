def file_replace(file_data):
    print("Replacing the file:",file_data)
    with open( file_data, 'r') as file:
     data = file.read()
     data = data.replace("&lt;", "<")
     data = data.replace("&gt;", ">")
     data = data.replace('<sub-log scm="git https://github.com/rajugajjela/git1.git">'," ")
     data = data.replace('<sub-log scm="git https://github.com/rajugajjela/project.git">'," ")
     data = data.replace("<multi-scm-log>"," ")
     data = data.replace("</multi-scm-log>"," ")
     data = data.replace("</sub-log>"," ")
  
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
    html_body=('<BODY> <table border=1><tr> <td>Commits</td><td>Commit Text</td></tr>')
    f = open('my_html.html','w')
    f.write(html_body)
    
    with open('changelog.xml', 'r') as f1:
     lines = f1.readlines()
    for i in range(len(lines)):
        if 'commit ' in lines[i]:
            commits=lines[i].split()[1]
            print(commits)
            f.write('<tr><td>%s</td> '%(commits))
        if 'committer ' in lines[i]:
            commit_text=lines[i+1]
            print(commit_text)
            f.write('<td>%s</td> <tr>'%(commit_text))
       
file_replace("changelog.xml")
remove_empty("changelog.xml")
new("changelog.xml")