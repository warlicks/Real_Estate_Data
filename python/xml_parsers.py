# Sean Warlick
# Seattle Housing Project
# XML Parsing Functions
# Date: July 12, 2016
###############################################################################
# Import packages
import xml.etree.ElementTree as et

def location_parse(xml_string):

	# Convert the data returned from api to XML
	xml_element = et.fromstring(xml_string) # Create to Element from string
	xml_tree = et.ElementTree(xml_element) # Convert Element to Element Tree

	
	# To correctly parse xml we need to idenitify the api funciton used. 
	parameters = xml_tree.findall(".//Parameter")

	# There are multiple Parameter nodes, we need to find the child name is "function"
	for p in parameters:
		if p.find("name").text == 'function':
			function = p.find('value').text
		else:
			next

	# To store the data parsed from xml we need to set up a variable.  We will use a dictionary with lists. 
	output = {"name":[], "code":[], "lon":[], "lat":[]}

	# Each API function has a slightly different schema, thus different logic to parse.  Following if statements set up the logic

	if function == 'getStates':
		data_node = xml_tree.findall('.//state')

		# Iterate through all state nodes & extract data
		for states in data_node:
			name = states.find('name').text
			output["name"].append(name)

			code = states.find('stateCode').text
			output["code"].append(code)

			lon = states.find('longitude').text
			output["lon"].append(lon)

			lat = states.find('latitude').text
			output["lat"].append(lat)

	elif function == 'getCountiesInState':
		data_node = xml_tree.findall('.//county')

		for county in data_node:
			name = county.find('name').text
			output["name"].append(name)

			lon = county.find('longitude').text
			output["lon"].append(lon)

			lat = county.find('latitude').text
			output["lat"].append(lat)

	elif function == 'getCitiesInState':
		data_node = xml_tree.findall('.//city')

		for city in data_node:
			name = city.find('name').text
			output["name"].append(name)

			lon = city.find('longitude').text
			output["lon"].append(lon)

			lat = city.find("latitude").text
			output["lat"].append(lat)


	elif function == 'getZipCodesInState':
		data_node = xml_tree.findall('.//zipCode')

		for code in data_node:
			ZIP = code.find('name').text
			output["code"].append(ZIP)

	elif function == 'getNeighborhoodsInCity':
		data_node = xml_tree.findall('.//neighborhood')

		for neighborhood in data_node:
			name = neighborhood.find('name').text
			output["name"].append(name)

	return output # Return output for use outside the function. 

def listing_parser(xml_string):

	# Convert the data returned from api to XML
	xml_element = et.fromstring(xml_string) # Create to Element from string
	xml_tree = et.ElementTree(xml_element) # Convert Element to Element Tree

	# To correctly parse xml we need to idenitify the api funciton used. 
	parameters = xml_tree.findall(".//Parameter")

	# There are multiple Parameter nodes, we need to find the child name is "function"
	for p in parameters:
		if p.find("name").text == 'function':
			function = p.find('value').text
		else:
			next
	print function

	# Set Up Storage For Parsed Data
	output = {"date":[], "type":[], "properties":[], "medianPrice":[], "avgPrice":[]}

	# Each API function has a slightly different schema, thus different logic to parse.  Following if statements set up the logic.

	## getStateStats parsing
	if function == 'getStateStats':
		data_node = xml_tree.findall(".//listingStat")

		for records in data_node:
			record_date = records.find("weekEndingDate").text # Extract record date
			
			categories = records.findall(".//subcategory") # Find all subcategory for the given weekend date
    
		for category in categories:
			output["date"].append(record_date) 

			tp = category.find("type").text
			output["type"].append(tp)

			prop = category.find("numberOfProperties").text
			output["properties"].append(prop)

			median = category.find("medianListingPrice").text
			output["medianPrice"].append(median)
        
			avg = category.find("averageListingPrice").text
			output["avgPrice"].append(avg)

	## getCityStats parsing
	elif function == 'getCityStats':
		data_node = xml_tree.findal(".//listingStat")

	return output