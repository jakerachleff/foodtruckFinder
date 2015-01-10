import os
import urllib
from urlparse import urlparse
import json
from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

@app.route('/')
def serverRequested():
	parsedURL = urlparse(request.url)
	if parsedURL.query == "":
		return getErrorResponse(400, "No query string")

	lat = request.args.get('lat')
	lon = request.args.get('lon')
	radius = request.args.get('radius')

	try:
		lat = float(lat)
		lon = float(lon)
		radius = float(radius)
	except:
		return getErrorResponse(400, "Malformed query string")

	if not checkValidLatLon(lat, lon):
		return getErrorResponse(400, "Latitude and longitude not in valid range")

	queryURL = "https://data.sfgov.org/resource/rqzj-sfat.json?$where=within_circle(location, %f, %f, %f)" % (lat, lon, radius)
	jsonurl = urllib.urlopen(queryURL)
	body = json.loads(jsonurl.read())
	response = jsonify({"status": 200, "body": body})
	response.status_code = 200
	return response

@app.errorhandler(404)
def notFound(error=None):
	return getErrorResponse(404, "Page not found")

@app.errorhandler(500)
def internalError(error=None):
	return getErrorResponse(500, "Internal server error")

def getErrorResponse(status, msg):
	response = jsonify({'status': status, 'body': msg})
	response.status_code = status
	return response

def checkValidLatLon(lat, lon):
	if((-90 <= lat <= 90) and (-180 <= lon <= 180)):
		return True
	return False

if __name__ == "__main__": 
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port, threaded=True)
