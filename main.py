import json
from http.client import responses

import requests
from datetime import date
from flask import Flask, jsonify,render_template

today = date.today()
app = Flask(__name__)
API_key = "c461613eec5144589c8d5a2ad1d64cd4"

# Top Headlines in the US
endpoint = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_key}"
response = requests.get(endpoint)

if response.status_code == 200:
    data = response.json()
else:
    print("Server Down")



@app.route('/news')
def get_news():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True, port=5001)

