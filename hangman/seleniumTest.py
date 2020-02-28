# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 08:49:20 2020

@author: palar
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://www.selenium.dev/documentation/en/")
assert "Python" in driver.title
elem = driver.find_element_by_id("Layer_1")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()