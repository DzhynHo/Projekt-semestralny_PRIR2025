from flask import Flask, render_template, abort
from pymongo import MongoClient
import certifi

app = Flask(__name__)

client = MongoClient(
    "mongodb+srv://valeriiakhylchenko:E4JSfcv8ytUWtBlH@cluster0.b6hq2v2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    tls=True,
    tlsCAFile=certifi.where()
)

db = client['buddhist']
coll = db['monasteries']

def clean_monastery(m):
    return {
        "name": m.get("name", "Невідомо"),
        "location": m.get("location", "Невідомо"),
        "gps": {
            "lat": m.get("gps", {}).get("lat", 0),
            "lon": m.get("gps", {}).get("lon", 0),
        },
        "website": m.get("website", ""),
        "image": m.get("image", ""),
        "description": m.get("description", "Опис відсутній."),
    }

@app.route("/")
def index():
    monasteries_raw = list(coll.find({}, {'_id': 0}))
    monasteries = [clean_monastery(m) for m in monasteries_raw if m.get("gps", {}).get("lat") and m.get("gps", {}).get("lon")]
    return render_template("map.html", monasteries=monasteries)

@app.route("/monasteries")
def monastery_list():
    monasteries_raw = list(coll.find({}, {'_id': 0, 'description': 0}))
    monasteries = [clean_monastery(m) for m in monasteries_raw]
    return render_template("monastery_list.html", monasteries=monasteries)

@app.route("/monasteries/<name>")
def monastery_detail(name):
    monastery_raw = coll.find_one({'name': name}, {'_id': 0})
    if not monastery_raw:
        abort(404)
    monastery = clean_monastery(monastery_raw)
    return render_template("monasteries.html", monastery=monastery)

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5003)
