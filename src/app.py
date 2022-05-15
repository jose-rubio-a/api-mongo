from pymongo import MongoClient
from flask import Flask, render_template, request, url_for, flash, redirect, abort
from bson.objectid import ObjectId
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '2dands4f4asd45a95s5dfd#'

def get_db_connection():
    client = MongoClient('mongodb+srv://admin:admin@cluster0.ephtx.mongodb.net/cluster0?retryWrites=true&w=majority')
    db = client.gettingStarted
    return db

def get_post(post_id):
    conn = get_db_connection()
    post = conn.posts.find_one({"_id": ObjectId(post_id)})
    if post is None:
        abort(404)
    return post

@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.posts
    return render_template('index.html', posts=posts.find())

@app.route('/<post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            post = {"title": title, "note": content, "created": datetime.today()}
            conn.posts.insert_one(post)
            return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/<id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.posts.update_one({"_id": ObjectId(id)}, {"$set": {"title": title, "note": content, "created": datetime.today()}})
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)

@app.route('/<id>/delete', methods=('POST',))
def delete(id):
    post = get_post(id)
    conn = get_db_connection()
    conn.posts.delete_one({"_id": ObjectId(id)})
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000, debug=True)