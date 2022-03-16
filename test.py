# import pytest
from array import array
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common import exceptions
from selenium.webdriver.common.by import By
import pandas as pd


driver = Chrome()
driver.implicitly_wait(10)

url = 'https://www.tokopedia.com/'
search_term = 'samsung a52'
driver.get(url)

# sleep(5)

# search_input = driver.find_element_by_xpath(
#       '//input[@aria-label="Search query"]')
# search_input = driver.find_element_by_xpath(
#     '//*[@id="search-container"]/form/div/div/div/input')
search_input = driver.find_element_by_xpath(
    '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[1]/input[1]')
search_input.send_keys(search_term)
search_input.send_keys(Keys.RETURN)
sleep(5)

lenOfPage = driver.execute_script(
    "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match = False
while(match == False):
   lastCount = lenOfPage
   sleep(7)
   lenOfPage = driver.execute_script(
       "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
   if lastCount == lenOfPage:
      match = True

sleep(10)
# limit = 10

items = []
data = pd.DataFrame()

# cards = driver.find_element_by_class_name('css-974ipl')
titles = driver.find_elements_by_class_name('css-1b6t4dn')
prices = driver.find_elements_by_class_name('css-1ksb19c')
rates = driver.find_elements_by_class_name('css-t70v7i')
sellers = driver.find_elements_by_class_name('css-1kdc32b')

# for seller in sellers:
#    print(seller.text)
# items.append(seller.text)
# data['title'] = items

for title in titles:
   # print(title.text)
   items.append(title.text)
data['title'] = items

items = []
for price in prices:
   # print(price.text)
   items.append(price.text)
data['price'] = items

items = []
for rate in rates:
   print(price.text)
   items.append(rate.text)
data['rate'] = items

print(data)
# print(title.text)
#    print(title.text)
# print(len(titles))
# try:
#    # name = driver.find_element_by_xpath(
#    #       '/html/body/div[1]/div/div[2]/div/div[2]/div[4]/div[1]/div[1]/div/div/div/div/div/div[2]/a/div[1]').text
#    name = driver.find_element(By.CLASS_NAME, "css-1b6t4dn")
#    print(name)
# except exceptions.NoSuchElementException:
#    name = ""

# /html/body/div[1]/div/div[2]/div/div[2]/div[4]/div[1]/div[1]
# /html/body/div[1]/div/div[2]/div/div[2]/div[4]/div[1]/div[1]
# /html/body/div[1]/div/div[2]/div/div[2]/div[4]/div[1]/div[1]/div/div/div/div/div/div[2]/a/div[1]
# /html/body/div[1]/div/div[2]/div/div[2]/div[4]/div[1]/div[1]/div/div/div/div/div/div[2]/a/div[2]

# lookback_limit = 25
# page_cards = driver.find_elements_by_xpath(
#     '/html/body/div[1]/div/div[2]/div/div[2]/div[4]/div[1]/div[1]')
# if len(page_cards) <= lookback_limit:
#    cards = page_cards
# else:
#    cards = page_cards[-lookback_limit:]


# def extract_data_from_current_tweet_card(card):
#    try:
#       name = card.find_element_by_xpath(
#           '/html/body/div[1]/div/div[2]/div/div[2]/div[4]/div[1]/div[1]/div/div/div/div/div/div[2]/a/div[1]').text
#       print(name)
#    except exceptions.NoSuchElementException:
#       name = ""

#    tweet = (name)
#    return tweet


# for card in cards:
#    try:
#       tweet = extract_data_from_current_tweet_card(card)
#    except exceptions.StaleElementReferenceException:
#       continue
# yield driver
# sleep(5)
driver.quit()
