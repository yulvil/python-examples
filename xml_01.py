
# http://docs.python.org/library/xml.etree.elementtree.html
# http://diveintopython3.org/xml.html

def writeToFile(filename, string):
    with open(filename, mode="w") as myFile:
        myFile.write(string)

writeToFile("sample.xml", """<?xml version="1.0"?>
<root>
   <sheet name="quebec" date="2011-02-03">
      <cell>11</cell>
      <cell>22</cell>
      <cell>33</cell>
   </sheet>
   <sheet name="ontario" date="2010-11-22">
      <cell>100</cell>
      <cell>200</cell>
      <cell>300</cell>
   </sheet>
   <sheet name="manitoba" date="2011-10-08">
      <cell>aa</cell>
      <cell>bb</cell>
      <cell>cc</cell>
   </sheet>
</root>""")

from xml.etree.ElementTree import ElementTree
doc = ElementTree(file='sample.xml')           # Load xml file in memory

l = [e.text for e in doc.findall('.//cell')]  # all the <cell> anywhere in the document
print(l)     # ['11', '22', '33', '100', '200', '300', 'aa', 'bb', 'cc']

l = [e.text for e in doc.findall('.//sheet/cell[2]')]  # second <cell> of any <sheet>
print(l)     # ['22', '200', 'bb']

l = [e.attrib for e in doc.findall('.//sheet')]  # second <cell> of any <sheet>
print(l)     # [{'date': '2011-02-03', 'name': 'quebec'}, {'date': '2010-11-22', 'name': 'ontario'}, {'date': '2011-10-08', 'name': 'manitoba'}]

l = [e.attrib['name'] for e in doc.findall('.//sheet')]
print(l)     # ['quebec', 'ontario', 'manitoba']

l = [e.get('name') for e in doc.findall('.//sheet')] # Same as above
print(l)     # ['quebec', 'ontario', 'manitoba']

print( doc.getroot()[2].attrib['date'] )     # 2011-10-08
print( doc.getroot()[2].get('date') )        # 2011-10-08

#l = [e.tostring() for e in doc.findall('.//sheet/cell[2]')]
#print( l )

#print( ElementTree.tostring(doc.getroot()[2]) )
