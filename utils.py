import urllib2, json

def fetchGoogleData(address):
    url = "http://maps.googleapis.com/maps/geocode/json?address=%s" %address
    request = urllib2.urlopen(url)
    jsonThing = url.read()
    result = json.loads(jsonThing)
    
    if result["status"] == "OK":
        latitude = result["results"][0]["geometry"]["location"]["lat"]
        longitude = result["results"][0]["geometry"]["location"]["lng"]
        place_id = result["results"][0]["geometry"]["place_id"]
