# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

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

    def maximize_window(self):
        self.driver.maximize_window()

    def dismiss_popup(self,id):
        self.driver.find_element_by_id(id).click()

    def scroll_page_down(self, path):
        component = self.driver.find_element_by_xpath('/html/body')
        component.send_keys(Keys.PAGE_DOWN).perform()
