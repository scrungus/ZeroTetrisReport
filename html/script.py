from bs4 import BeautifulSoup
import re

with open('litrev.html','r') as f:
    contents = f.read()
    tag = "<sup class=\"textsuperscript\">"

    m = re.finditer(tag,contents)
    matches_pos = [match.start() for match in m]

count = 0
for i in matches_pos:
    contents = contents[:i+count] + "^" + contents[i+count:]
    count += 1

with open('litrev.html','w') as f:
    f.write(contents)
