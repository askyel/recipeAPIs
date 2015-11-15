import urllib2, json

def nytArticleSearch(tag):
    nytKey="7d9f3b88013d99f9f9ab2a8a82545671:19:73424493" #new york times article search api key
    url= "http://api.nytimes.com/svc/search/v2/articlesearch.json?fq=source:(%s)&q=%s&api-key=%s"
    url=url%("The+New+York+Times",tag,nytKey)
    request = urllib2.urlopen(url)
    result = request.read()
    r = json.loads(result)
    return r

print nytArticleSearch('burger')
