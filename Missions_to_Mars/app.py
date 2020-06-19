from flask import Flask, render_template, redirect
import scrape_mars
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars"
mongo = PyMongo(app)

@app.route("/")
def index():
    mars_info = mongo.db.mars_info.find_one()
    return render_template("index.html", mars_info = mars_info)

@app.route("/scrape")
def scraper():
    mars_results = scrape_mars.scrape()

    mars_info = mongo.db.mars_info
    mars_info.update({}, mars_results, upsert=True)

    return redirect("/", code = 302)

# @app.route("/table_mars")
# def table():
#     mars_info = mongo.db.mars_info.find_one()["table"]
#     return render_template("ttable.html", mars_info = mars_info)

if __name__ == "__main__":
    app.run(debug=True)

