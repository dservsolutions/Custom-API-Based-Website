import os
import requests
from dotenv import load_dotenv
from datetime import date
from flask import Flask, render_template


today = date.today()

app = Flask(__name__)
app.config['SECRET_KEY'] = "ZJ\x9e\xc74N\x8d\xe5\xe8\x05\xd2w\xab\xbe\\\xe2+\x01\xac\x9c\x94\xa7\xfbc"

load_dotenv() # Load environment variables from .env if it exists
api_key = os.getenv("API_KEY")

# Top Headlines in the US
endpoint = f"https://newsapi.org/v2/top-headlines?"
parameters = {"country": "us",
              "apiKey": {api_key}
              }
response = requests.get(endpoint, params=parameters)
data = response.json()

@app.route('/', methods = ["GET", "POST"])
def get_news():
    articles = data['articles']
    top_news = articles[0]
    return render_template('index.html',
                           article = articles,
                           top_news=top_news)

if __name__ == "__main__":
    app.run(debug=True, port=5001)

