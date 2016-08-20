# Import Libriaries
###############################################################################
import urllib
import xml.etree.ElementTree as et
import pandas as pd

# Define Global Variable
###############################################################################
trulia = 'http://api.trulia.com/webservices.php?' # Set Trulia URL

# Define function to call trulia API and parse the returned XML
###############################################################################
def county_stats(county, state, start_date, end_date, api_key):
	
	# Set Up URL for API Call
	url = trulia + urllib.urlencode({'library':'TruliaStats', 'function':'getStateStats', 'state':state, 'county':county, 'startDate':start_date, 'endDate':end_date, 'apikey':api_key}) # Create url

	# Connect to API
	page = urllib.urlopen(url) 
	xml_string = page.read()

	# Create dictionary for storage of parsed xml
	output = {"date":[], "state":[], "county":[], "type":[], "properties":[], "medianPrice":[], "avgPrice":[]}

	# Convert the data returned from api to XML
	xml_element = et.fromstring(xml_string) # Create to Element from string
	xml_tree = et.ElementTree(xml_element) # Convert Element to Element Tree
	
	# Parse the XML
	data_node = xml_tree.findall(".//listingStat")

	for records in data_node:
		record_date = records.find("weekEndingDate").text # Extract record date
			
		categories = records.findall(".//subcategory") # Find all subcategory for the given weekend date
    
		for category in categories:
			output["date"].append(record_date) 

			output["state"].append(state)
			output["county"].append(county)

			tp = category.find("type").text
			output["type"].append(tp)

			prop = category.find("numberOfProperties").text
			output["properties"].append(prop)

			median = category.find("medianListingPrice").text
			output["medianPrice"].append(median)
        
			avg = category.find("averageListingPrice").text
			output["avgPrice"].append(avg)

	data_frame = pd.DataFrame(output) # Convert to a data frame for easy import in R
	return data_frame