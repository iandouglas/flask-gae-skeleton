# coding: utf-8
from google.appengine.ext import db


class User(db.model):
    _use_memcache = True
    _use_cache = True

    guser = db.UserProperty(required=True, auto_current_user=False, indexed=True)

    username = db.StringProperty()
    name = db.StringProperty()
    email = db.StringProperty()
