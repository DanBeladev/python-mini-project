import requests

class BasePost:
    def __init__(self, user_id: int, id: int, title: str, body: str):
        self.user_id = user_id
        self.id = id
        self.title = title
        self.body = body

URL = "https://jsonplaceholder.typicode.com/posts"
r = requests.get(URL)
payload = r.json()

posts = {}
for p in payload:
    post = BasePost(p['userId'], p['id'], p['title'], p['body'])
    posts[post.id] = post

