Documentation for Foodtruck Finder:


Foodtruck finder will return a json containing two values: status and body. Status will always contain the http response code. Body will contain one of two things. In the case of a status code of 200, body will contain a list of all json entries of nearby foodtrucks. Each entry will contain data mentioned in "fields" at the following link: http://dev.socrata.com/foundry/#/data.sfgov.org/rqzj-sfat

In all other cases, body will contain an error message describing what went wrong.

To correctly access foodtruck finder, one must type in the url for the server followed by a query string consisting of three floats: lat, lon, and radius (ex: https://nameless-bastion-3232.herokuapp.com/?lat=37.79&lon=-122.4&radius=300). 

lat and lon are the client's latitude and longitude, and radius is the farthest distance as the crow flies that the client would go to a foodtruck.

Foodtruck Finder is hosted on heroku, and its base url is https://nameless-bastion-3232.herokuapp.com
