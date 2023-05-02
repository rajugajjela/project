lines = []
with open('changelog.xml', 'r') as file:
     data = file.read()
     data = data.replace("&lt;", "<")
     data = data.replace("&gt;", ">")
     data = data.replace("&amp;quot;","" "")
     data = data.replace("<multi-scm-log>"," ")
     data = data.replace("</multi-scm-log>"," ")
     data = data.replace("</sub-log>"," ")
     data = data.replace("&apos;","'")
     data = data.replace("&quot;","'")
     # data = data.replace("<sub-log scm")

with open('changelog.xml', 'w') as file:
    file.write(data)

with open('changelog.xml', 'r') as file:
     lines=file.readlines()

with open('changelog.xml', 'w') as file:

    for number, line in enumerate(lines):
       if number not in [1, 45, 78]:
        file.write(line)

