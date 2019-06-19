# coding: utf-8
from google.appengine.ext import db


class SitemapContent(db.Model):
    _use_memcache = True
    _use_cache = True

    content_type = db.StringProperty(required=True, default='Application/xml')
    url = db.StringProperty(required=True)
    body = db.BlobProperty()

    # only index things that are public to everyone
    indexed = db.BooleanProperty(required=True, default=True)

    created = db.DateTimeProperty(auto_now_add=True)
    created_by = db.UserProperty(auto_current_user_add=True)
    modified = db.DateTimeProperty(auto_now=True)
    modified_by = db.UserProperty(auto_current_user=True)
