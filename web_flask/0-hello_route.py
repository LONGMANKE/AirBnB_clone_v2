#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'

@app.route('/airbnb-onepage/', strict_slashes=False)
def airbnb_onepage():
    """returns a response for /airbnb-onepage/"""
    return 'Welcome to AirBnB OnePage!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
