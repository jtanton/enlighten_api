#########################################################################################
## usage: python get-solarinfo.py [-h] -e endpoint
##
## Python script to get enphaseenergy system summary using Enlighten API
##		James Tanton
#		Created : 9/26/2018
#		Updated : 2/17/2019
## 		Help on getting started - https://developer.enphase.com/docs/quickstart.html	
##		
##		Your KEY and user values will be unique to your system of course
##		Log into enphase to get your system id from the browser url
##
## Usage:
##   optional arguments:
##     -h, --help  show this help message and exit
##
##   required arguments:
##     -e endpoint    Enlighten API endpoint (summary, inventory, etc)
#########################################################################################

import requests, json, pprint, os, argparse

def getcontent(URL):
	"""

	:rtype: data
	"""
	print (URL)
	#print URL # Debug line comment out or remove
	r = requests.get(URL) #Fetching response from URL
	print ('get processed') # Debug line as well
	print (r.content) # Display unformated json response
	data = json.loads(r.text) # Format as JSON
	print ('raw data: \n' + str(r.content) )
	print ('\n pprinted json:')
	pprint.pprint(data)
	#rtype: data
	return data

# Sample URL 
# URL='https://api.enphaseenergy.com/api/v2/systems/{your system id}/summary?key=xxxxxxx&user_id=xxxxxxx'
# '/arrays?range=today&view=energy_production'

## MAIN
# Grab all the required arguments from the command line.
parser = argparse.ArgumentParser(description='Call Enphase API to fetch data',
                                 usage = 'python get-solarinfo.py [-h] -e endpoint')
requiredArgs = parser.add_argument_group('required arguments')
requiredArgs.add_argument('-e', action='store',
                          required = True,
                          dest='endpoint',
                          help='Name of the Enlighten Systems endpoint. e.g. consumption_lifetime,consumption_stats,energy_lifetime, envoys, index, inventory, monthly_production, production_meter_readings, rgm_stats, stats, summary, arrays?range=today&view=energy_production ',)
inputargs = parser.parse_args()

print (inputargs.endpoint)

SITE = 'https://api.enphaseenergy.com/api/v2'
#KEY = '?key=XXXXXX&user_id=XXXX'
apikey = os.environ.get("apikey")
siteid = os.environ.get("siteid")+"/"
userid = os.environ.get("userid")
KEY = "?key="+apikey+"&user_id="+userid

# Call getcontent for systems. 
APICALL = '/systems/' + siteid + inputargs.endpoint
URL=SITE+APICALL+KEY
print ( URL )
getcontent(URL)
