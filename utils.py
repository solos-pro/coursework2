import json

def load_data():
    with open('data/data.json') as fp:
        posts = json.load(fp)

    with open('data/comments.json') as fp:
        comments = json.load(fp)

    posts = attach_comments_to_posts(posts, comments)

    with open('data/bookmarks.json') as fp:
        bookmark = json.load(fp)

    return posts, comments, bookmark



def attach_comments_to_posts(posts, comments):
    for i, post enumerate(posts):
        pk = post.get('pk')
        post_comments = []
        for comment in comments:
            if comment.get('post_id') == pk:
                post_comments.append(comment)
            posts[i]['comment_count'] = len(post_comments)
        return posts
