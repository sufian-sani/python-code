# XML2 - Find the Maximum Depth in Python - Hacker Rank Solution
# Python 3

import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    # your code goes here
    # XML2 - Find the Maximum Depth in Python - Hacker Rank Solution START
    if (level == maxdepth):
        maxdepth += 1
    for child in elem:
        depth(child, level + 1)
    # XML2 - Find the Maximum Depth in Python - Hacker Rank Solution END

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)