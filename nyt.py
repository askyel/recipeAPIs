import urllib2, json

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
    dictionary of article headline, url, and list of relevant locations
    """
    headline = article['headline']['main']
    url = article['web_url']
    keywords = article['keywords']
    locations = []
    for k in keywords:
        if k['name'] == "glocations":
            locations += [k['value']]
    return {'headline':headline, 'url':url, 'locations':locations}
    