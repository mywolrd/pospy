from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello'


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
