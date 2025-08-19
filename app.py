from flask import Flask, render_template
import requests

app = Flask(__name__)

API_KEY = "376d864df6c24745e0b2eb75e2cc0037"  # replace with your real key
BASE_URL = "https://gnews.io/api/v4/top-headlines"

@app.route("/")
def home():
    return "<h2>Welcome to My Indian News App 📰</h2><p>Go to <a href='/india-news'>India News</a></p>"

@app.route("/india-news")
def india_news():
    params = {
        "country": "in",
        "lang": "en",
        "token": API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    news_data = response.json()
    articles = news_data.get("articles", [])
    return render_template("news.html", articles=articles)

if __name__ == "__main__":
    app.run(debug=True)

