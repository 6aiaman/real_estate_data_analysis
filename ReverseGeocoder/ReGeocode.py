from lat_lng1 import *

import requests
import json
import time
from random import randint
import csv

# Create and write in csv file.
with open( "my_address_components.csv", "w") as f:
	output = csv.writer(f)
	i = 1

# Google Reverse Geocoding.
	for ll in lat_lng:
		# sleeps
		time.sleep(.1)
		postal_code = ''

		def get_address():
			try:
				raw_address = requests.get('http://maps.googleapis.com/maps/api/geocode/json?latlng=' + ll )
				full_address = raw_address.json()
				my_full_address = full_address['results'][0]['address_components']	
				if my_full_address:
					for component in my_full_address:
					    if ('postal_code' in component['types']):
					        postal_code = component['long_name']
					print(postal_code)
					output.writerow([i, postal_code])
				else:
					raw_address = requests.get('http://maps.googleapis.com/maps/api/geocode/json?latlng=' + ll )
					full_address = raw_address.json()
					my_full_address = full_address['results'][0]['formatted_address"']
					print(my_full_address)
					output.writerow([i, my_full_address])
			except:
				print("N/A {}".format(i))
				output.writerow([i])
				pass

		get_address()		
		i += 1










