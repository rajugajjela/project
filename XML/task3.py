import xml.etree.ElementTree as ET
file_data="""<?xml version='1.0' encoding='UTF-8'?>
<list>
    <hudson.plugins.repo.ChangeLogEntry>
        <commitText>
#44024- Version Change
versionName &quot;6.0.2&quot;
</commitText>
        <revision>d76a168de515f2b</revision>
        <committerName>Dummy </committerName>
        <serverPath> OCRLibapp </serverPath>
        <committerDate>2022-08-29 05:56:09</committerDate>
    </hudson.plugins.repo.ChangeLogEntry>
    <hudson.plugins.repo.ChangeLogEntry>
        <commitText>
Reverted to owl2 version to avoid confusion
</commitText>
        <revision>e3b5950a5ad218e</revision>
        <committerName>Dummy </committerName>
        <serverPath> OCRLibapp </serverPath>
        <committerDate>2022-08-29 05:38:30</committerDate>
    </hudson.plugins.repo.ChangeLogEntry>
    <hudson.plugins.repo.ChangeLogEntry>
        <commitText>
#436736 - RELM-003 OCR lib changeaccuracy improved OCR engine  (DynaEye) given by PFU for m-release
</commitText>
        <revision>c148b335cf8aceb</revision>
        <committerName>Dummy </committerName>
        <serverPath> OCRLibapp </serverPath>
        <committerDate>2022-08-29 05:38:30</committerDate>
    </hudson.plugins.repo.ChangeLogEntry>
    <hudson.plugins.repo.ChangeLogEntry>
        <commitText>
Gradle and size constraint changes
</commitText>
        <revision>93528503b5d0ff1</revision>
        <committerName>Dummy </committerName>
        <serverPath> OCRLibapp </serverPath>
        <committerDate>2022-08-29 05:38:29</committerDate>
    </hudson.plugins.repo.ChangeLogEntry>
</list>
"""
my_file = ET.fromstring(file_data)
for x in my_file.findall('hudson.plugins.repo.ChangeLogEntry'):
    commit_text=x.find('commitText').text
    commits=x.find('revision').text
    print("commitText is:",commit_text)
    print("commit is:",commits)
    print("\n")