import requests
from flask import Flask
app = Flask(__name__)

@app.route('/some-url')
def get_data():
    print(requests.get('https://randomuser.me/api/ ').content)
    return requests.get('https://randomuser.me/api/ ').content
