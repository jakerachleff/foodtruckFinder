Documentation for Foodtruck Finder:

Foodtruck finder will return a json containing two values: status and body. Status will always contain the http response code. Body will contain one of two things. In the case of a status code of 200, body will contain all json entries of nearby foodtrucks. In all other cases, body will contain an error message describing what went wrong.

To correctly access foodtruck finder, one must type in the url for the server ("   /") followed by a query string containing three floats: lat, lon, and radius. Lat and Lon are the client's latitude and longitude, and radius is the farthest distance as the crow flies that the client would go to a foodtruck. All foodtrucks in radius of position (lat, long) will be returned in the body field of the json.
