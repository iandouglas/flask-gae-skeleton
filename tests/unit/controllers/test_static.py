# coding=utf-8
import unittest
from google.appengine.ext import testbed
from run import app


class StaticPages(unittest.TestCase):
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

    def test_home(self):
        resp = self.tc.get('/')
        self.assertIn('Hello world', resp.data)

    def test_privacy(self):
        resp = self.tc.get('/privacy')
        self.assertTrue('Privacy Notice' in resp.data)
        self.assertTrue('Google Analytics' in resp.data)
        self.assertTrue('Google AdSense' in resp.data)

    def test_robotstxt(self):
        resp = self.tc.get('/robots.txt')
        self.assertIn('User-agent: *', resp.data)
        self.assertIn('Sitemap: http://iandouglas.com/sitemap.xml', resp.data)
