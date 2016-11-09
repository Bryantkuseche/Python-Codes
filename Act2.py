import re
import urllib
from bs4 import BeautifulSoup

#Getting Data
url = raw_input("Enter: ")
count = raw_input("Enter count: ")
position = raw_input("Enter Position: ")

#Convert to valid data
count = int(count)
position = int(position)
position = position - 1
x = 0

#Engine and all the magic thing

while x < count:
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html) 
	txt = soup.find_all('a')
	lst = list()
	for index in txt:
		lst.append((index.get('href')))
	url = str(lst[position])
	x = x + 1
	#Printing the answer
	print 'Retrieving: ' , url
	
