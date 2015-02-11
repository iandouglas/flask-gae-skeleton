# coding=utf-8
from splinter import Browser
import unittest
from google.appengine.ext import testbed

browser = Browser()


class StaticPagesTest(unittest.TestCase):
    def setUp(self):
        global browser
        self.tb = testbed.Testbed()
        self.tb.activate()
        self.tb.init_memcache_stub()

    def tearDown(self):
        self.tb.deactivate()

    def test_splinter_social_linkedin(self):
        browser.visit('http://127.0.0.1:8080/')
        self.assertEqual(browser.is_text_present('iandouglas.com'), True)
        browser.click_link_by_partial_href('linkedin.com')
        self.assertIn('https://www.linkedin.com/', browser.url)

    def test_zzzzz_last_test(self):
        browser.quit()
