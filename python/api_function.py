# Sean Warlick
# Seattle Housing Project
# Turila API Data Collection
# Date Created: July 7, 2016)
###############################################################################

# Import Needed Library
###############################################################################
import urllib
#import api

# Define Global Variables 
###############################################################################

trulia = 'http://api.trulia.com/webservices.php?' # Set Trulia URL


# Set enviromental variables
###############################################################################
location_functions = ['getCitiesInState', 'getCountiesInState', 'getNeighborhoodsInCity', 'getStates', 'getZipCodesInState']

stat_functions = ['getCityStats', 'getCountyStats', 'getNeighborhoodStats', 'getStateStats', 'getZipCodesStats'] # List of stat functions for error checking


# Create a function to list the avaliable options for the LocationInfo Library.
###############################################################################
def location_options():
	print 'Avaliable Location Functions Are: \n'
	for option in location_functions:
		print option, ', \n'

# Create a function to list the avaliable options for the LocationInfo Library.
###############################################################################
def stat_options():
	print 'Avaliable Stats Functions Are: \n'
	for option in stat_functions:
		print option, ', \n'


# Define Function for locationInfo API
###############################################################################
def location_api(function, city, state, api_key):
	
	# Check that function parameter is valid
	if function not in location_functions: 
	 	print 'Check Specified Function' 		
		
	# When function is correct execute API call
	else: 
		url = trulia + urllib.urlencode({'library':'LocationInfo', 'function':function, 'city':city, 'state':state, 'apikey':api_key}) # Create url

		# Connect to API
		page = urllib.urlopen(url) 
		data = page.read()
		return data # Make data accesable outside of function. 

# Define function to call state_stats
###############################################################################
def state_stats(state, start_date, end_date, api_key):

	# Set Up URL for API Call
	url = trulia + urllib.urlencode({'library':'TruliaStats', 'function':'getStateStats', 'state':state, 'startDate':start_date, 'endDate':end_date, 'apikey':api_key}) # Create url

	# Connect to API
	page = urllib.urlopen(url) 
	data = page.read()
	return data # Make data accesable outside of function. 

# Define Function to call getCityStats
###############################################################################
def city_stats(city, state, start_date, end_date, api_key):

	# Set Up URL for API Call
	url = trulia + urllib.urlencode({'library':'TruliaStats', 'function':'getCityStats', 'city':city, 'state':state, 'startDate':start_date, 'endDate':end_date, 'apikey':api_key}) # Create url

	# Connect to API
	page = urllib.urlopen(url) 
	data = page.read()
	return data # Make data accesable outside of function.