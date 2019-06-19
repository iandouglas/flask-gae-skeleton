# coding=utf-8
import unittest
from google.appengine.ext import testbed
from application import create_app
from application.utils import sanitize_input


class UtilityFunctions(unittest.TestCase):
    def setUp(self):
        self.tb = testbed.Testbed()
        self.tb.activate()
        self.tb.init_memcache_stub()
        self.tb.init_urlfetch_stub()

        self.app = create_app('testing')
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        self.tb.deactivate()

    def test_user_sanitize(self):
        test_string = sanitize_input('Test<script>alert()</script>')
        self.assertEqual(test_string, 'Test&lt;script&gt;alert()&lt;/script&gt;')
