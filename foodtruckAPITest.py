import urllib
import json


def main():
	wellFormedTest()
	wrongPathTest()
	nonFloatLatLongRadiusTest()

def wellFormedTest():
	print("Running test of well-formed query")
	wellFormedResponse = jsonOpenURL("https://nameless-bastion-3232.herokuapp.com/?lat=37.7901&lon=-122.399&radius=300")
	print("Expected Status: 200\nActual Status: %d") % wellFormedResponse['status']
	queryResults = wellFormedResponse['body']
	print("Show all trucks within 300 meters of latitude=37.7901, longitude=-122.399: ")
	for truck in queryResults:
		print("\t%s") % truck['applicant']
	print("")

def wrongPathTest():
	print("Running test of requesting a non existant path")
	wrongPathResponse = jsonOpenURL("http://nameless-bastion-3232.herokuapp.com/badpath/")
	print("Expected Status: 404\nActual Status: %d") % wrongPathResponse['status']
	print("Expected Body: Page not found\nActual Body: %s\n") % wrongPathResponse['body']

def nonFloatLatLongRadiusTest():
	print("Running test of non numeric lat, long, and radius")
	testMalformedInputs("37.77", "-122.22", "notAFloat", "Malformed query string") 
	testMalformedInputs("37.77", "notAFloat", "500", "Malformed query string")
	testMalformedInputs("notAFloat", "-122.22", "500", "Malformed query string")

	print("Running test of out of range latitude and longitude")
	testMalformedInputs("37.77", "-189", "500", "Latitude and longitude not in valid range")
	testMalformedInputs("37.77", "189", "500", "Latitude and longitude not in valid range")
	testMalformedInputs("-99", "-122.22", "500", "Latitude and longitude not in valid range")
	testMalformedInputs("99", "-122.22", "500", "Latitude and longitude not in valid range")

def testMalformedInputs(lat, lon, radius, error):
	url = "http://nameless-bastion-3232.herokuapp.com/?lat=%s&lon=%s&radius=%s" % (lat, lon, radius)
	print("Running test where lat=%s, lon=%s, radius=%s") % (lat, lon, radius)
	malformedQueryResponse = jsonOpenURL(url)
	print("Expected Status: 400\nActual Status: %d") % malformedQueryResponse['status']
	print("Expected Body: %s\nActual Body: %s\n") % (error, malformedQueryResponse['body'])

def jsonOpenURL(url):
	jsonurl = urllib.urlopen(url)
	return json.loads(jsonurl.read())

if __name__ == "__main__":
	main()
