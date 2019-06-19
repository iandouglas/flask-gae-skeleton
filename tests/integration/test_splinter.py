# coding=utf-8
from splinter import Browser
import unittest
from google.appengine.ext import testbed


@unittest.skip("Skipping splinter tests (they still need work)")
class HomepageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = Browser()

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

    def setUp(self):
        self.tb = testbed.Testbed()
        self.tb.activate()
        self.tb.init_memcache_stub()

    def tearDown(self):
        self.tb.deactivate()

    def test_splinter_homepage(self):
        self.browser.visit('http://127.0.0.1:8080/')
        self.assertEqual(self.browser.is_text_present('iandouglas.com'), True)
