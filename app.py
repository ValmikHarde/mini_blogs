from flask import Flask, render_template, request, redirect, url_for, flash
import csv
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = "mini_blog_secret"

CSV_FILE = "blog_posts.csv"


# ---------- Helper Functions ----------
def load_posts():
    posts = []
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                posts.append(row)
    return posts


def save_posts(posts):
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        fieldnames = ["id", "title", "description", "content", "timestamp"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(posts)


# ---------- Routes ----------
@app.route("/", methods=["GET", "POST"])
def index():
    posts = load_posts()

    # Search filter
    search_query = request.args.get("search", "").lower()
    if search_query:
        posts = [p for p in posts if search_query in p["title"].lower()]

    return render_template("index.html", posts=posts, search_query=search_query)


@app.route("/add", methods=["GET", "POST"])
def add_post():
    if request.method == "POST":
        title = request.form["title"].strip()
        description = request.form["description"].strip()
        content = request.form["content"].strip()

        if not title or not description or not content:
            flash("All fields are required!", "danger")
            return redirect(url_for("add_post"))

        posts = load_posts()
        new_id = str(len(posts) + 1)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        posts.append({
            "id": new_id,
            "title": title,
            "description": description,
            "content": content,
            "timestamp": timestamp
        })

        save_posts(posts)
        flash("Post added successfully!", "success")
        return redirect(url_for("index"))

    return render_template("add_post.html")


@app.route("/post/<id>")
def view_post(id):
    posts = load_posts()
    post = next((p for p in posts if p["id"] == id), None)
    if not post:
        flash("Post not found!", "danger")
        return redirect(url_for("index"))
    return render_template("view_post.html", post=post)


@app.route("/edit/<id>", methods=["GET", "POST"])
def edit_post(id):
    posts = load_posts()
    post = next((p for p in posts if p["id"] == id), None)

    if not post:
        flash("Post not found!", "danger")
        return redirect(url_for("index"))

    if request.method == "POST":
        title = request.form["title"].strip()
        description = request.form["description"].strip()
        content = request.form["content"].strip()

        if not title or not description or not content:
            flash("All fields are required!", "danger")
            return redirect(url_for("edit_post", id=id))

        post["title"] = title
        post["description"] = description
        post["content"] = content
        post["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        save_posts(posts)
        flash("Post updated successfully!", "success")
        return redirect(url_for("view_post", id=id))

    return render_template("edit_post.html", post=post)


@app.route("/delete/<id>")
def delete_post(id):
    posts = load_posts()
    posts = [p for p in posts if p["id"] != id]
    save_posts(posts)
    flash("Post deleted successfully!", "success")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
