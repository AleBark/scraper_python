# -*- coding: utf-8 -*-
from selenium import webdriver

"""
Ale Bark Bruneri
"""


class HtmlHandler(object):

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Firefox()
        self.driver.get(url)
        self.html = self.driver.page_source

    def get_html(self):
        return self.html
