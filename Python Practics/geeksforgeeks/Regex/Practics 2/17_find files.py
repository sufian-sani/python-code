import re

regex=re.compile('\.xml$')

filenames = ["gfg.html", "geeks.xml","computer.txt", "geeksforgeeks.jpg", "filesearch.xml"]

for file in filenames:
    if re.search(regex,file):
        print("The file ending with .xml is:",file)
    else:
        print("Invalid")