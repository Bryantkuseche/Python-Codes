import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter - ')
num = 0
cont = 0
txt = ''
print 'Retrieving: ', url
fhand = urllib.urlopen(url)
data = fhand.read()
print 'Retrieved ', len(data) , 'characters'
tree = ET.fromstring(data)
	
counts = tree.findall('.//count')
for index in counts:
	txt = index.text
	txt = float(txt)
	num = num + txt
	cont = cont + 1

print 'Count: ' , cont
print 'Sum: ', num

