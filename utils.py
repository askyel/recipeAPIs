import urllib2, json

def fetchLatLng(address):
    #replace whitespaces in address with a +
    address = address.replace(" ", "+")
    print address
    url = "https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=AIzaSyDK9pqvEWsu7SWG9b6eZp6KuXKZwM_qQR4" % address
    print url
    request = urllib2.urlopen(url)
    jsonThing = request.read()
    result = json.loads(jsonThing)
    l = {}
    if result["status"] == "OK":
        l["lat"] = result["results"][0]["geometry"]["location"]["lat"]
        l["lng"] = result["results"][0]["geometry"]["location"]["lng"]
        #place_id = result["results"][0]["geometry"]["place_id"]
    print l
    return l


def fetchRecipes(ingredients):
    # ingredients is a list of the five ingredients requested
    query = ''
    for i in ingredients:
        query = query+i
        query = query+'%20'
    query = query[0:-3]
    url = 'https://api.edamam.com/search?q=' + query+ '&app_id=821b9133&app_key=5fd301b3c02db28eba7b9cdfed7ee453'
    request = urllib2.urlopen(url)
    results = request.read()
    r = json.loads(results)
    recipes = r['hits']
    if len(recipes) > 10:
        recipes = recipes[0:10]
    return recipes
#print r['hits'][0]['recipe']['ingredients']
#print r['hits'][0]['recipe']['url']
#print r['hits'][0]['recipe']['image']
fetchLatLng("345 Chambers Street")
