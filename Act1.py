import urllib
import re
from bs4 import BeautifulSoup

#Getting URL

ads = raw_input("Enter - ")
html = urllib.urlopen(ads)

#Getting Text

soup = BeautifulSoup(html)

#Processing Text
num2 = ''
count = 0
num = 0
txt = soup.get_text()
x = re.findall('[0-9]+', txt)
for index in x:
	num2 = index
	num2 = float(num2)
	num = num + num2
	count = count + 1
 	
#Printing Results

print count
print num


