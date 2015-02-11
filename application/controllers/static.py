# coding: utf-8
from flask import render_template


def home():
    return render_template('home.html')


def privacy():
    return render_template('static/privacy.html')


def robots_txt():
    return '''User-agent: *

Sitemap: http://iandouglas.com/sitemap.xml
'''
