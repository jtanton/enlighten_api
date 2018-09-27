''' 
		Python script to get enphaseenergy system summary using Enlighten API
		James Tanton 9/26/2018

		Help on getting started
	  		https://developer.enphase.com/docs/quickstart.html	
		
		Your KEY and user values will be unique to your system of course
		Log into enphase to get your system id from the browser url

'''

import requests, json, pprint

def getcontent(URL):
	print URL # Debug line comment out or remove
	r = requests.get(URL) #Fetching response from URL
	print 'get processed' # Debug line as well
	print r.content # Display unformated json response
	data = json.loads(r.text) # Format as JSON
	print data 
	print 'pprinted json \n'
	pprint.pprint(data)
	
# Sample URL 
# URL='https://api.enphaseenergy.com/api/v2/systems/{your system id}/summary?key=xxxxxxx&user_id=xxxxxxx'


SITE = 'https://api.enphaseenergy.com/api/v2'
KEY = '?key=XXXXXX&user_id=XXXX'


# Call x - Test call for Energy Production

APICALLX = '/systems/484/arrays?range=today&view=energy_production'
URL=SITE+APICALLX+KEY
#getcontent(URL)


# Call 1 - Summary
APICALL = '/systems/484/summary'
URL=SITE+APICALL+KEY
getcontent(URL)

# Call 2 - Systems
APICALL2 = '/systems'
URL=SITE+APICALL2+KEY
#getcontent(URL)


APICALL3 = '/systems/484/energy_lifetime'
APICALL4 = '/systems/484/consumption_stats'
APICALL4 = '/systems/484/envoys'
