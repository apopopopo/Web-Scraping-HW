from flask import Flask, render_template, jsonify, redirect
import pymongo
import scrape_mars
import pandas as pd

app = Flask(__name__)


client = pymongo.MongoClient()
db = client.mars_db
collection = db.mars




@app.route("/")
def index():
	mars = mongo.db.mars.find_one()
	return render_template("index.html", mars=mars)


@app.route("/scrape")
def scrape():
    mars = mongo.db.listings
    mars_data= scrape_mars.scrape()
    mars.update(
    {},
    mars_data,
    upsert=True
    )
    return redirect("http://localhost:5000/", code=302)


if __name__ == "__main__":
    app.run(debug=True)