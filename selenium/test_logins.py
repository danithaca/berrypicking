#!/usr/local/bin/python3.4
# vim:ts=4:sw=4:sts=4:tw=80
###############################################################################
### FILENAME : test_logins.py
### AUTHOR   : jczyz@quadmetrics.com
### CREATED  : 2015-03-23
### TYPE     : Testing Module
### PURPOSE  : Tests Front End Login
### REQUIRES : selenium (pip3.4 install it...), utils module, Firefox
### TODOS    : *

"""
test_logins.py : test suite for exercising our front page login system


"""

###############################################################################
### IMPORTS
import re
import unittest

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

###############################################################################
### GLOBAL CONSTANTS

WWW_URL = 'https://www.quadmetrics.com'

TEST_ACCOUNT = 'foobar@quadmetrics.com'  #FIXME
TEST_PASS = '' #FIXME


###############################################################################
### FUNCTIONS
class TestWWWLogins(unittest.TestCase):

    def setUp(self):
        browser = webdriver.Firefox()
        browser.get(WWW_URL)
        self.browser = browser
        self.addCleanup(self.browser.quit)

    def test_login_fail(self):
        browser = self.browser
        elem = browser.find_element_by_link_text("Login")
        elem.click()
        elem = browser.find_element_by_id("email")
        elem.send_keys(TEST_ACCOUNT)
        elem = browser.find_element_by_id("password")
        elem.send_keys('invalid_pass')
        elem.send_keys(Keys.ENTER)
        text_found = re.search(
            r"we don't recognize the email/password combination",
            browser.page_source)
        self.assertTrue(bool(text_found))


if __name__ == '__main__':
        unittest.main()
#EOF
