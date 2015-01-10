#Foodtruck Finder API

##Client Access of Nearby Locations

To access nearby locations, the client must provide three pieces of information: latitude, longitude, and radius. Radius refers to the maximum distance (as the crow flies) the client would travel to find a food truck in meters. All requests must be sent to a url with a valid query string in the following format:

	"http://nameless-bastion-3232.herokuapp.com/?lat=<lat>&lon=<lon>&radius=<radius>"

Latitude must be between -90 and 90 degrees, and longitude must be between -180 and 180 degrees. Radius must be given, there is no "default radius."

##API JSON Response

The Foodtruck Finder Application returns a json with two fields: status and body.

####Status

Status contains the HTTP status code (200, 400, 404, or 500).

####Body

Body contains one of two things: an error message, or a list of json entries to DataSF's database of foodtrucks in San Francisco

######Error Message

When the HTTP status code is not 200, body contains a short error message describing what went wrong. For example, if the query string in the url is not correctly formed, the error message will read "Malformed query string."

######Database Entries

Each entry in the list will have the following fields:


* locationid
* applicant
* facilitytype
* cnn
* locationdescription
* address
* blocklot
* block
* lot
* permit
* status
* fooditems
* x
* y
* latitude
* longitude
* schedule
* noisent
* approved
* Received
* priorpermit
* expirationdate
* location

For more information on each field, visit the [database's API documentation] (http://dev.socrata.com/foundry/#/data.sfgov.org/rqzj-sfat)

#Prior Experience With Stack

###Prior Python Experience
Last summer, I learned python to create a script to convert pharmaceutical data from NCPDP format to human readable csv files. This consisted of mostly string manipulation and file IO.

###Prior Flask Experience
This is my first flask application, as well as my first web application.
