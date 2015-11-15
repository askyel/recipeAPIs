<<<<<<< HEAD
from flask import Flask, render_template
import urllib2, json
=======
from flask import Flask, render_template, request, redirect, url_for
>>>>>>> b6ec614b80fd6fe95ae2ac61fc6fc0c0b5b4a1a5

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("master.html")

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/search", methods=["GET", "POST"])
def search():
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
		return render_template("search.html", results=results)

@app.route("/result")
@app.route("/result/<recipe>")
def result():
	recipe_info = {}  # dictionary of recipe information from __ API
			  # includes name, ingredients, photo
	articles = []  # list of food safety articles relevant to ingredients
        map_info = {}
	return render_template("result.html", recipe_info=recipe_info, articles=articles,map_info=map_info)

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0',port=8000)
