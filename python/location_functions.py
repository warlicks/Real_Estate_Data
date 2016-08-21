# Sean Warlick
# Seattle Housing Project
# Turila API Data Collection
# Date Created: July 7, 2016)
###############################################################################

# Import Needed Library
###############################################################################
import urllib
import pandas as pd
import xml.etree.ElementTree as et

# Define Global Variable
###############################################################################
trulia = 'http://api.trulia.com/webservices.php?' # Set Trulia URL

# Define Function To Return Cities in State.
###############################################################################
def get_cities(state, api_key):

	# Set Up URL for API Call
	url = trulia + urllib.urlencode({'library':'LocationInfo', 'function':"getCitiesInState", 'state':state, 'apikey':api_key}) # Create URL

	# Connect to API
	page = urllib.urlopen(url) 
	xml_string = page.read()

	# Create Storage Dictionary
	output = {"name":[], "code":[], "lon":[], "lat":[]}

	# Convert the data returned from api to XML
	xml_element = et.fromstring(xml_string) # Create to Element from string
	xml_tree = et.ElementTree(xml_element) # Convert Element to Element Tree

	data_node = xml_tree.findall('.//city')

	for county in data_node:
		name = county.find('name').text
		output["name"].append(name)

		output["code"].append(state)

		lon = county.find('longitude').text
		output["lon"].append(lon)

		lat = county.find('latitude').text
		output["lat"].append(lat)
	
	# Prepare data for use outside function. 
	data_frame = pd.DataFrame(output) # Convert to a data frame for easy import in R
	return data_frame

# Define Function To Return Cities in State.
###############################################################################
def get_neighborhood(city, state, api_key):
	# Set Up URL for API Call
	url = trulia + urllib.urlencode({'library':'LocationInfo', 'function':"getNeighborhoodsInCity", 'city':city, 'state':state, 'apikey':api_key}) # Create URL

	# Connect to API
	page = urllib.urlopen(url) 
	xml_string = page.read()
	
	# Create Storage Dictionary
	output = {"name":[], "id":[]}

	# Convert the data returned from api to XML
	xml_element = et.fromstring(xml_string) # Create to Element from string
	xml_tree = et.ElementTree(xml_element) # Convert Element to Element Tree
	
	#Parse XML
	data_node = xml_tree.findall('.//neighborhood')

	for neighborhood in data_node:
		name = neighborhood.find('name').text
		iD = neighborhood.find('id').text
			
		output["name"].append(name)
		output["id"].append(iD)

	data_frame = pd.DataFrame(output)
	return data_frame

# Define Function To Return Cities in State.
###############################################################################
def get_zipcode(state, api_key):

	# Set Up URL for API Call
	url = trulia + urllib.urlencode({'library':'LocationInfo', 'function':"getZipCodesInState", 'state':state, 'apikey':api_key}) # Create URL

	# Connect to API
	page = urllib.urlopen(url) 
	xml_string = page.read()
	
	# Create Storage Dictionary
	output = {"state":[], "code":[]}

	# Convert the data returned from api to XML
	xml_element = et.fromstring(xml_string) # Create to Element from string
	xml_tree = et.ElementTree(xml_element) # Convert Element to Element Tree
	
	#Parse XML
	data_node = xml_tree.findall('.//neighborhood')

	for code in data_node:
		output["state"].append(state)

		ZIP = code.find('name').text
		output["code"].append(ZIP)

	data_frame = pd.DataFrame(output)
	return data_frame

# Define Function To Return Counties in State.
###############################################################################
def get_counties(state, api_key):

	# Set Up URL for API Call
	url = trulia + urllib.urlencode({'library':'LocationInfo', 'function':"getCountiesInState", 'state':state, 'apikey':api_key}) # Create URL

	# Connect to API
	page = urllib.urlopen(url) 
	xml_string = page.read()
	
	# Create Storage Dictionary
	output = {"state":[], "name":[], "lon":[], "lat":[]}

	# Convert the data returned from api to XML
	xml_element = et.fromstring(xml_string) # Create to Element from string
	xml_tree = et.ElementTree(xml_element) # Convert Element to Element Tree

	# Parse XML
	data_node = xml_tree.findall('.//county')

	for county in data_node:
		output["state"].append(state)

		name = county.find('name').text
		output["name"].append(name)

		lon = county.find('longitude').text
		output["lon"].append(lon)

		lat = county.find('latitude').text
		output["lat"].append(lat)

	data_frame = pd.DataFrame(output)
	return data_frame


# Define Function To Return List of States
###############################################################################
def get_states(api_key):

	# Set Up URL for API Call
	url = trulia + urllib.urlencode({'library':'LocationInfo', 'function':"getStates", 'apikey':api_key})

	# Connect to API
	page = urllib.urlopen(url) 
	xml_string = page.read()


	# Create Storage
	output = {"name":[], "code":[], "lon":[], "lat":[]}

	# Convert the data returned from api to XML
	xml_element = et.fromstring(xml_string) # Create to Element from string
	xml_tree = et.ElementTree(xml_element) # Convert Element to Element Tree

	# Parse XML
	data_node = xml_tree.findall('.//state')
	
	for states in data_node:
		name = states.find('name').text
		output["name"].append(name)

		code = states.find('stateCode').text
		output["code"].append(code)

		lon = states.find('longitude').text
		output["lon"].append(lon)

		lat = states.find('latitude').text
		output["lat"].append(lat)

	data_frame = pd.DataFrame(output)
	return data_frame	




















