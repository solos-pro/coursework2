from flask import Flask, request, render_template, url_for
from utils import *
import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))
path_basedir = os.path.join(BASEDIR)
path_css = os.path.join(BASEDIR, 'css')
path_img = os.path.join(BASEDIR, 'img')

posts, comments, bookmarks = load_data()

app = Flask(__name__, static_url_path='/static')


@app.route('/',)
def page_index():
    # return 'server works'
    return render_template('index.html', posts=posts)

@app.route("/search/")
def search_page():
    search_query = request.args.get("word")
    searched_posts = []
    if search_query:
        for post in posts:
            if search_query in post["content"]:
                post["content"] = post["content"][:50]
                searched_posts.append(post)

    return render_template("search.html", posts=searched_posts, num=len(searched_posts))

# with app.test_request_context():
#     print(url_for('/search/'))

app.run(debug=True)
