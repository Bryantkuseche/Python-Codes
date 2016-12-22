import re, os


fname = raw_input("Enter file name: ")
print "Searching Trackers..."

data = open(fname)

http = list()
num_link_http = 0
udp = list()
num_link_udp = 0
for link in data:
	link = link.rstrip()
	if re.search('http://.*' , link):
		http.append(link)
		num_link_http = num_link_http + 1
	elif re.search('udp://.*' , link):
		udp.append(link)
		num_link_udp = num_link_udp + 1
for link in http:
	hostname = link
	response = os.system("ping -c 1 " + hostname)
	#and then check the response...
	if response == 0:
		print hostname, 'is up!'
	else:
		print hostname, 'is down!'


for link in udp:
	hostname = link 
	response = os.system("ping -c 1 " + hostname)

	#and then check the response...
	if response == 0:
		print hostname, 'is up!'
	else:
		print hostname, 'is down!'



print "Statistics:\n"
print "There is" , num_link_http , "Http's links"
print "There is" , num_link_udp ,  "Udp's links" 
