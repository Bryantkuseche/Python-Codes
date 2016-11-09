import urllib
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
	direccion = raw_input("Enter Location: ")
	if len(direccion) < 1:
		print "Good Bye"
		break
	url = serviceurl + urllib.urlencode({'sensor':'false', 'address': direccion}) 
	print 'Retrieving ' , url
	uh = urllib.urlopen(url)
	data = uh.read()
	print 'Retrieved',len(data),'characters'
	try: js = json.loads(str(data))
	except: js = None
	
	placeid = js["results"][0]["place_id"]
	print 'Place ID:', placeid
	
