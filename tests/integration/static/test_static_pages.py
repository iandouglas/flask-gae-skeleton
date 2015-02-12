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

    def test_splinter_privacy(self):
        browser.visit('http://127.0.0.1:8080/')
        self.assertEqual(browser.is_text_present('iandouglas.com'), True)
        browser.click_link_by_text('privacy')
        self.assertEqual(browser.is_text_present('Privacy Notice'), True)

    def test_robots_txt(self):
        browser.visit('http://127.0.0.1:8080/robots.txt')
        self.assertIn('User-agent: *', browser.html)
        self.assertIn('Sitemap: http://iandouglas.com/sitemap.xml', browser.html)

    def test_zzzzz_last_test(self):
        browser.quit()
