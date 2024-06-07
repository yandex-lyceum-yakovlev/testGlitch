from flask import Flask
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

@app.route('/index')
def index():
    return f"Hello index"

@app.route('/secret')
def secret():
    SECRET = os.getenv("SECRET")
    return f"Secret = {SECRET}"

@app.route('/')
def root():
    return "Hello"


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')
