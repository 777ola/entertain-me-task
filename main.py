import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/task")
def task():
    ENDPOINT = "http://www.boredapi.com/api/activity"
    r = requests.get(ENDPOINT)
    task = r.json()['activity']
    return render_template('page.html', task=task)


if __name__ == "__main__":
    app.run(debug=True)