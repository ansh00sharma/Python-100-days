from flask import Flask, render_template
import time
import requests
from post import Post;

app = Flask(__name__)

fake_blog_url  = "https://api.npoint.io/7d935070cbe97a8c0f47"
response = requests.get(fake_blog_url)
posts = response.json()
all_posts = []

for item in posts:
    post_obj = Post(item['id'],item['title'],item['subtitle'],item['body'])
    all_posts.append(post_obj)


@app.route("/blog")
def blogpage():
    return render_template("generic.html", posts=all_posts)


@app.route("/post/<int:index>")
def data(index):
    specific_post = all_posts[index-1]
    return render_template("post.html", blog=specific_post)

if __name__ == "__main__":
    app.run(debug=True)