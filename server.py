from flask import Flask
import os
from dotenv import load_dotenv

app = Flask(__name__)


@app.route('/index')
def index():
    SECRET = os.getenv("SECRET")
    return f"Hello index {SECRET}"


@app.route('/')
def root():
    return "Hello"


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')
