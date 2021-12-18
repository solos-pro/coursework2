import json
from pprint import pprint


def load_data():
    with open('data/data.json') as fp:
        posts = json.load(fp)

    with open('data/comments.json') as fp:
        comments = json.load(fp)

    posts = prepare_posts(posts, comments)

    with open('data/bookmarks.json') as fp:
        bookmark = json.load(fp)

    return posts, comments, bookmark



def prepare_posts(posts, comments):
    for i, post in enumerate(posts):
        pk = post.get('pk')
        post_comments = []
        for comment in comments:
            if comment.get('post_id') == pk:
                post_comments.append(comment)
            posts[i]['comment_count'] = len(post_comments)

        posts[i]['content'] = tegify_content(posts[i]['content'])
        pprint(posts)
    return posts

# pprint(load_data())

def tegify_content(content):
    words = content.split(" ")
    for i, word in enumerate(words):
        if word.startswith("#"):
            tag = word.replace("#", "")
            link = f"<a href='/tag/{tag}>'{word}</a>"
            words[i] = link
    print(words)
    print(" ".join(words))
    return " ".join(words)

tegify_content("#egg #peece world #travel")