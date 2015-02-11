# # coding=utf-8
import unittest
import uuid
from google.appengine.ext import testbed
from application import create_app
from application.routes import create_routes


class FlaskClient(unittest.TestCase):
    def setUp(self):
        self.tb = testbed.Testbed()
        self.tb.activate()
        self.tb.init_memcache_stub()
        self.tb.init_urlfetch_stub()

        self.app = create_app('testing')
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        self.tb.deactivate()

    def test_flask(self):
        self.assertIsNotNone(self.app)

    def test_routes(self):
        create_routes(self.app)
        self.assertIsNotNone(self.app.url_map)

        rule_count = 0
        expected_static_endpoints = 5

        for _ in self.app.url_map.iter_rules():
            rule_count += 1
        self.assertGreaterEqual(rule_count, expected_static_endpoints)

    def test_404(self):
        response = self.client.get('/%s' % uuid.uuid4())
        self.assertEqual(response.status_code, 404)

    def test_static_route_for_404(self):
        response = self.client.get('/404')
        self.assertEqual(response.status_code, 404)
