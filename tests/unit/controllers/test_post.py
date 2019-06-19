# coding=utf-8
import unittest
from google.appengine.api import users
from google.appengine.ext import testbed
from application.models.post import Post
from run import app


class PostModel(unittest.TestCase):
    def setUp(self):
        self.tb = testbed.Testbed()
        self.tb.activate()
        self.tb.setup_env(USER_EMAIL='admin@example.com', USER_ID='1', USER_IS_ADMIN='1', overwrite=True)
        self.tb.init_datastore_v3_stub()
        self.tb.init_memcache_stub()
        self.tb.init_user_stub()

    def tearDown(self):
        self.tb.deactivate()

    def test_guser_current(self):
        guser = users.get_current_user()
        self.assertEqual(guser.email(), 'admin@example.com')

    def test_create_post(self):
        guser = users.get_current_user()

        Post(title='fake post title').put()
        new_post = Post.find_by_properties(title='fake post title')

        self.assertIsNotNone(new_post.created)
        self.assertEqual(new_post.created_by, guser)
        self.assertIsNotNone(new_post.modified)
        self.assertEqual(new_post.modified_by, guser)
