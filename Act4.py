import json
import urllib

url = raw_input("Enter location: ")
print 'Retrieving ' , url

uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved ', len(data) , 'characters'

js = json.loads(data)
lst = js['comments']
txt = ''
num = 0
cont = 0
for index in lst:
	 txt = index["count"]
	 txt = float(txt)
	 num = num + txt
	 cont = cont + 1
print 'Count' , cont
print 'Sum' , num
	

