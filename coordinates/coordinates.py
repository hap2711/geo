#!/bin/python

import requests
import pprint

def get_coordinates():
	url='https://maps.googleapis.com/maps/api/geocode/json?'
	address=input("Enter location: ")
	response = requests.get(url,params={'address':address})
	if response.json()['status']!="ZERO_RESULTS":
	    # API response
	    json_response=response.json()

	    # Latitude and Longitude
	    lat = json_response['results'][0]['geometry']['location']['lat']
	    lng = json_response['results'][0]['geometry']['location']['lng']

	    print("Latitude: {}".format(lat))
	    print("Longitude: {}".format(lng))

	    # Area Name
	    formatted_address=json_response['results'][0]['formatted_address']
	    pprint.pprint(formatted_address)
	else:
	    print(response.json()['status'])


