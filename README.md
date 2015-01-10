#Foodtruck Finder API

##Client Access of Nearby Locations

To access nearby locations, the client must provide three pieces of information: latitude, longitude, and radius. Radius refers to the maximum distance (as the crow flies) the client would travel to find a food truck. All requests must be sent to a url with a valid query string in the following format:

	"http://nameless-bastion-3232.herokuapp.com/?lat=<lat>&lon=<lon>&radius=<radius>"

##API JSON Response

The Foodtruck Finder Application returns a json with two fields: status and body.

###Status

Status contains the HTTP status code (200, 400, 404, or 500)

###Body

Body contains one of two things: an error message or a list of json entries to the database of foodtrucks in San Francisco

#####Error Message

When the HTTP status code is not 200, body contains a short error message describing what went wrong.

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
