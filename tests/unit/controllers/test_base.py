# coding=utf-8
import unittest
from google.appengine.ext import testbed
from run import app


class BaseSite(unittest.TestCase):
    def setUp(self):
        self.tb = testbed.Testbed()
        self.tb.activate()
        self.tb.setup_env(USER_EMAIL='home@example.com', USER_ID='1', USER_IS_ADMIN='0', overwrite=True)
        self.tb.init_user_stub()
        self.tb.init_datastore_v3_stub()
        self.tb.init_memcache_stub()
        self.tc = app.test_client()

    def tearDown(self):
        self.tb.deactivate()

    def test_base(self):
        resp = self.tc.get('/')
        self.assertIn('iandouglas.com', resp.data)
        self.assertIn('Ian at Google+', resp.data)
        self.assertIn('Ian at LinkedIn', resp.data)
        self.assertIn('Ian at GitHub', resp.data)
        self.assertIn('Ian at Twitter', resp.data)

        self.assertIn('home', resp.data)
        self.assertIn('ramblings and musings of a senior webdev', resp.data)

        self.assertIn('privacy', resp.data)
        self.assertIn('copyright &copy; 1996-<span class="flask-moment" data-timestamp="', resp.data)
