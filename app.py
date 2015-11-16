from flask import Flask, render_template, request, redirect, url_for, session
import utils, nyt
import urllib2, json

app = Flask(__name__)

global recipes
recipes = {}

@app.route("/")
def index():
	return render_template("master.html")

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/search", methods=["GET", "POST"])
def search():
	global recipes
	if request.method=="GET":
		return render_template("search.html", results=[])
	else:
		ing1 = request.form["ing1"]
		ing2 = request.form["ing2"]
		ing3 = request.form["ing3"]
		ing4 = request.form["ing4"]
		ing5 = request.form["ing5"]
		query = [ing1,ing2,ing3,ing4,ing5]
		results = utils.fetchRecipes(query)  # list of recipes matching ingredients
		for r in results:
			name = r['recipe']['label']  
			if name not in recipes:
				recipes[name] = r['recipe']
		return render_template("search.html", results=results)

@app.route("/result")
@app.route("/result/<recipe>")
def result(recipe=""):
	global recipes
	recipe_info = recipes[recipe]  # dictionary of recipe information from Edamam API
	articles = []  # list of food safety articles relevant to ingredients
        #latlng=utils.fetchLatLng(address) # We need to get the address from the article
	return render_template("result.html", recipe_info=recipe_info, articles=articles)#,fetchLatLng=fetchLatLng)

@app.route("/nyt/<tag>")
def nyt():
        return nyt.nytArticleSearch(tag)
        
if __name__ == "__main__":
    app.debug = True
    app.secret_key="0112358"
    app.run(host='0.0.0.0',port=8000)
