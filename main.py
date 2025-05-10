import requests
from datetime import date
from flask import Flask, render_template

today = date.today()
app = Flask(__name__)
API_key = "c461613eec5144589c8d5a2ad1d64cd4"

# Top Headlines in the US
endpoint = f"https://newsapi.org/v2/top-headlines?"
parameters = {"country": "us",
              "apiKey": {API_key}
              }
response = requests.get(endpoint, params=parameters)
data = response.json()

# articles = data['articles']
# for i in range(10):
#     if i < len(articles):
#         article = articles[i]
        # print(f"Processing article at index {i}: {article['title']}")


@app.route('/', methods = ["GET", "POST"])
def get_news():
    articles = data['articles']
    top_news = articles[0]
    return render_template('index.html',
                           article = articles,
                           top_news=top_news)

if __name__ == "__main__":
    app.run(debug=True, port=5001)

