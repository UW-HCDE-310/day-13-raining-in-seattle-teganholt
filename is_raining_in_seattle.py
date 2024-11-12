from flask import Flask
import urllib.request

app = Flask(__name__)

def is_it_raining_in_seattle():
    with urllib.request.urlopen('https://depts.washington.edu/ledlab/teaching/is-it-raining-in-seattle/') as response:
        is_it_raining_in_seattle = response.read().decode()

    if is_it_raining_in_seattle == "true":
        return "<h1>Yes</h1>"
    else:
        return "<h1>No</h1>"

@app.route('/')
def check_rain():
    return is_it_raining_in_seattle()

if __name__ == '__main__':
    app.run(debug=True)