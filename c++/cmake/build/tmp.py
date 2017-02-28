import xml.etree.ElementTree

e = xml.etree.ElementTree.parse('/home/muhmud/code/c++/projects/test2/build/.project')
n = e.find('name')
n.text = 'proj'
e.write('/home/muhmud/test.xml')
