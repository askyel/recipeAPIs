import urllib2, json

def fetchGoogleData(address):
    url = "http://maps.googleapis.com/maps/geocode/json?address=" % address
    request = urllib.urlopen(url)
    jsonThing = url.read()
    result = json.loads(jsonThing)
    l = {}
    if result["status"] == "OK":
        l["lat"] = result["results"][0]["geometry"]["location"]["lat"]
        l["lng"] = result["results"][0]["geometry"]["location"]["lng"]
        #place_id = result["results"][0]["geometry"]["place_id"]
    return l
