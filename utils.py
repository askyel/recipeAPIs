import urllib2, json

def fetchGoogleData(address):
    key = "AIzaSyDK9pqvEWsu7SWG9b6eZp6KuXKZwM_qQR4"
    url = "http://maps.googleapis.com/maps/geocode/json?adress="+address+"&key="+key
    request = urllib.urlopen(url)
    jsonThing = url.read()
    latitude = jsonThing["results"]["geometry"]["location"]["lat"]
    longitude = jsonThing["results"]["geometry"]["location"]["lng"]
