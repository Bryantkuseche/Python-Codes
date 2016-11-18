import re

fname = raw_input("Enter file name: ")
print "Searching Trackers..."

data = open(fname)

http = list()
num_link_http = 0
udp = list()
num_link_udp = 0
magnet = list()
magnet_num = 0
for link in data:
	link = link.rstrip()
	if re.search('http://.*' , link):
		http.append(link)
		num_link_http = num_link_http + 1
	elif re.search('udp://.*' , link):
		udp.append(link)
		num_link_udp = num_link_udp + 1
	elif re.search('magnet:.*', link):
		magnet.append(link)
		magnet_num = magnet_num + 1
		

for link in http:
	print link

for link in udp:
	print link

print "Statistics:\n"
print "There is" , num_link_http , "Http's links"
print "There is" , num_link_udp ,  "Udp's links" 
print "There is" , magnet_num , "Magnet's links"
