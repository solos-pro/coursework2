from flask import Flask, request, render_template
from utils import *

posts, comments, bookmarks = load_data()

app = Flask(__name__)

@app.route('/',)
def page_index():
    # return 'server works'
    return render_template('index.html', posts=posts)

@app.route("/search/")
def search_page():
    name = request.args.get("s")
    with open("candidates.json") as f:
        candidates = json.load(f)
    users = []
    if name:
        for candidate in candidates:
            if name in candidate["name"]:
                users.append(candidate["name"])

    return render_template("search.html", users=users, cnt=len(users))

app.run(debug=True)
