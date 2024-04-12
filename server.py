from flask import Flask

app = Flask(__name__)


@app.route('/index')
def index():
    return "Hello index"


@app.route('/')
def root():
    return "Hello"


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')
