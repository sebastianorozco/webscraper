from splinter import Browser
import pandas as pd

url = "https://www.google.com"

browser = Browser('chrome')  # open a chrome browser
browser.visit(url)  # goes to the url

search_bar_xpath = '//*[@id="lst-ib"]'
search_bar = browser.find_by_xpath(search_bar_xpath)[0]  # find_by_xpath returns a list, so index 0
search_bar.fill("CodingStartups.com")  # simulate typing


search_button_xpath = '//*[@id="tsf"]/div[2]/div[3]/center/input[1]'
search_button = browser.find_by_xpath(search_button_xpath)[0]
search_button.click()  # simulate clicking


search_results_xpath = '//h3[@class="r"]/a'
search_results = browser.find_by_xpath(search_results_xpath)  # returns list of link elements

