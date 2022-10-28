import json


def load_posts(path='posts.json'):
    posts = []
    with open(path, 'r', encoding='utf8') as file:
        posts = json.load(file)
    return posts


def search_post(substr):
    posts_found = []
    posts = load_posts()
    for post in posts:
        if substr in post["content"]:
            posts_found.append(post)
    return posts_found


