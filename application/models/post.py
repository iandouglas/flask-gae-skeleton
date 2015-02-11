# coding: utf-8
from google.appengine.ext import db


class Post(db.Model):
    _use_memcache = True
    _use_cache = True

    stub = db.StringProperty(indexed=True)
    title = db.StringProperty(indexed=True)
    body = db.TextProperty()
    publish_date = db.DateProperty(auto_now_add=True)

    created = db.DateTimeProperty(auto_now_add=True)
    created_by = db.UserProperty(auto_current_user_add=True)
    modified = db.DateTimeProperty(auto_now=True)
    modified_by = db.UserProperty(auto_current_user=True)

    @classmethod
    def find_by_properties(cls, **kwargs):
        return cls.find_all_by_properties(**kwargs).get()

    @classmethod
    def find_all_by_properties(cls, **kwargs):
        query = cls.all()
        for name, value in kwargs.items():
            query = query.filter('{prop_name} = '.format(prop_name=name), value)
        return query
