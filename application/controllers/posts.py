# coding: utf-8
from flask import request, url_for, redirect
from google.appengine.api import users
from application.models.post import Post
from application.utils import sanitize_input


def save_post():
    guser = users.get_current_user()
    if not guser:
        return redirect(url_for('home'))

    post = Post()
    post.stub = sanitize_input(request.form['stub'])
    post.title = sanitize_input(request.form['title'])
    post.body = sanitize_input(request.form['body'])
    post.publish_date = sanitize_input(request.form['publish_date'])
    post.put()
