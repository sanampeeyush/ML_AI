from flask import Flask
app = Flask(__name__)

@app.route('/')
def sample():
    return 'kuch bhi sample'

@app.route('/new')
def new():
    return '<h1>This is heading</h1>'

app.run(debug=True)


# google.com
# https://www.google.com/
# https://www.google.com/search
# https://www.google.com/search?q="kuch search hua"






