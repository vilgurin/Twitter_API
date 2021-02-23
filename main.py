from flask import Flask, render_template, request
from Lab3Task3 import twitter_data,get_location_and_name,folium_map
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    if not request.form.get("domain") or \
        folium_map(get_location_and_name(twitter_data(request.form.get("domain")))) == "failure" :
            return render_template("failure.html")
    else:
        followers = folium_map(get_location_and_name(twitter_data(request.form.get("domain"))))
    return followers._repr_html_()

if __name__ == "__main__":
    app.run(debug = True)
