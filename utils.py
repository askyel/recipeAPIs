import urllib2, json

######### Google Maps API #############

def fetchLatLng(address):
    """
    Fetches data from the Google Maps Geocoding API.
    
    Arguments:
    address -- string name of a location
    
    Returns:
    dictionary of floats for latitude and longitude of address
        'lat' -- latitude of address
        'lng' -- longitude of address
    """
    #replace whitespaces in address with a +
    address = address.replace(" ", "+")
    #print address
    url = "https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=AIzaSyDK9pqvEWsu7SWG9b6eZp6KuXKZwM_qQR4" % address
    #print url
    request = urllib2.urlopen(url)
    jsonThing = request.read()
    result = json.loads(jsonThing)
    l = {}
    if result["status"] == "OK":
        l["lat"] = result["results"][0]["geometry"]["location"]["lat"]
        l["lng"] = result["results"][0]["geometry"]["location"]["lng"]
        #place_id = result["results"][0]["geometry"]["place_id"]
    #print l
    return l

def createMarker(address):
    """
    Creates marker string based on address formatted for Google Maps API url.
    
    Arguments:
    address -- string name of a location
    
    Returns:
    if latitude and longitude can be found,
        string to create marker in Google map, labeled by first letter of address
    otherwise,
        empty string
    """
    latLng = fetchLatLng(address)
    if 'lat' in latLng and 'lng' in latLng:
        return "&markers=color:red%7Clabel:"+address[0].upper()+"%7C"+str(latLng['lat'])+","+str(latLng['lng'])
    else:
        return ""

def markers(articleList):
    """
    Compiles marker strings for listed articles.
    
    Arguments:
    articleList -- list of dictionaries of article information
    
    Returns:
    string of markers formatted for Google Maps API url
    """
    markerString = ""
    for article in articleList:
        for l in article['locations']:
            markerString += createMarker(l)
    return markerString

########### Edamam Recipe API #############

def fetchRecipes(ingredients):
    """
    Fetches recipes from the Edamam API.

    Arguments:
    ingredients -- list of ingredients to search recipes for

    Returns:
    list of 10 or fewer recipe dictionaries from Edamam API
    """
    # ingredients is a list of the five ingredients requested
    query = ''
    for i in ingredients:
        query = query+i
        query = query+'%20'
    query = query[0:-3]
    url = 'https://api.edamam.com/search?q=' + query + '&app_id=821b9133&app_key=5fd301b3c02db28eba7b9cdfed7ee453'
    request = urllib2.urlopen(url)
    results = request.read()
    try: 
        r = json.loads(results)
    except ValueError:
        return []
    recipes = r['hits']
    if len(recipes) > 10:
        recipes = recipes[0:10]
    return recipes

def recipeIngredients(recipeInfo):
	"""
	Extracts a list of food names from a dictionary of recipe information.

	Arguments:
	recipe-info -- dictionary of recipe information from Edamam API

	Returns:
	list of food names in the recipe
	"""
	foods = []
	ings = recipeInfo['ingredients']
	for i in ings:
		foods += [i['food']]
	return foods
    
########## NY Times Article Search API ##########

def safeSearch(ing):
    """
    Makes string safe as query term for NY Times API
    
    Arguments:
    ing -- query term
    
    Returns
    string with '+' instead of ' '
    """
    return "+".join(ing.split(" "))

def nytArticleSearch(tag):
    """
    Fetches list of news articles related to search term.
    
    Arguments:
    tag -- search term
    
    Returns:
    list of dictionaries of article information
    """
    nytKey="7d9f3b88013d99f9f9ab2a8a82545671:19:73424493" #new york times article search api key
    url= 'http://api.nytimes.com/svc/search/v2/articlesearch.json?q=%s&fq=type_of_material:("News")&api-key=%s'
    url=url%(tag,nytKey)
    request = urllib2.urlopen(url)
    result = request.read()
    r = json.loads(result)
    return r['response']['docs']
    
def extractInfo(article):
    """
    Extracts relevant article information from article dictionary.
    
    Arguments:
    article -- dictionary of information returned by NY Times API
    
    Returns:
    dictionary of article information
        headline -- article title
        url - article web url
        locations -- list of relevant locations to article
    """
    headline = article['headline']['main']
    url = article['web_url']
    keywords = article['keywords']
    locations = []
    for k in keywords:
        if k['name'] == "glocations":
            locations += [k['value']]
    return {'headline':headline, 'url':url, 'locations':locations}

def articleList(ingList):
    	"""
    	Creates a list of articles relevant to a list of ingredients.
    
    	Arguments:
    	ingList -- list of ingredients
    
   	    Returns:
    	list of dictionaries with article information for each ingredient
    	"""
    	articles = []
	for ing in ingList:
            ingArticles = nytArticleSearch(safeSearch(ing))
            if len(ingArticles) > 5:  # limit to 5 articles per ingredient
                ingArticles = ingArticles[0:5]
        	for article in ingArticles:
            		info = extractInfo(article)
            		articles += [info] 
    	return articles 
