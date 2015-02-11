# coding=utf-8
from splinter import Browser
import unittest
from google.appengine.ext import testbed

browser = Browser()


class HomepageTest(unittest.TestCase):
    def setUp(self):
        global browser
        self.tb = testbed.Testbed()
        self.tb.activate()
        self.tb.init_memcache_stub()

    def tearDown(self):
        self.tb.deactivate()

    def test_splinter_homepage(self):
        browser.visit('http://127.0.0.1:8080/')
        self.assertEqual(browser.is_text_present('iandouglas.com'), True)

    def test_zzzzz_last_test(self):
        browser.quit()
