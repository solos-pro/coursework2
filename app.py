from flask import Flask, request, render_template
from utils import *

posts, comments, bookmarks = load_data()

app = Flask(__name__)

@app.route('/',)
def page_index():
    # return 'server works'
    return render_template('index.html', posts=posts)

app.run(debug=True)
