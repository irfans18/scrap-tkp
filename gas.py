# import pytest
from array import array
from warnings import catch_warnings
from numpy import append
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import pandas as pd


driver = Chrome()
driver.implicitly_wait(10)

url = 'https://www.tokopedia.com/'
search_term = 'xiaomi'
driver.get(url)

# sleep(5)

# search_input = driver.find_element_by_xpath(
#       '//input[@aria-label="Search query"]')
# search_input = driver.find_element_by_xpath(
#     '//*[@id="search-container"]/form/div/div/div/input')
search_input = driver.find_element(
    By.XPATH, '//input[@aria-label="Bidang pencarian"]')
search_input.send_keys(search_term)
search_input.send_keys(Keys.RETURN)
sleep(5)

# driver.find_element_by_xpath('//button[@data-testid="CPMShopButton"]').click()


# scroll
y = 1000
for timer in range(0, 10):
   driver.execute_script("window.scrollTo(0, "+str(y)+")")
   y += 600
   sleep(3)

# this scrolls untill the element is in the middle of the page
# lenOfPage = driver.execute_script(
#     "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
# match = False
# while(match == False):
#    lastCount = lenOfPage
#    sleep(7)
#    lenOfPage = driver.execute_script(
#        "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
#    if lastCount == lenOfPage:
#       match = True
# element = driver.find_element_by_xpath('//div[@class="css-70qvj9"]')
# driver.execute_script("arguments[0].scrollIntoView();", element)


# sleep(10)
# limit = 10

titles, prices, rates = [], [], []
data = pd.DataFrame()


catalog = driver.find_element(
    By.XPATH, '//div[@data-testid="divSRPContentProducts"]')
container = catalog.find_elements(
    By.XPATH, './/div[@class="css-jza1fo"]')
cards = catalog.find_elements(
    By.XPATH, './/div[@class="css-12sieg3"]')
# cards = catalog.find_elements_by_class_name('css-12sieg3')


# print("Total container : ", len(container))
# print("Total cards : ", len(cards))
# driver.find_element(By.XPATH, "//button[@aria-label='Halaman berikutnya']").click()


# count = 0
for card in cards:
   title = card.find_element(
       By.XPATH, './/div[@class="css-1b6t4dn"]').text
   price = card.find_element(
       By.XPATH, './/div[@class="css-1ksb19c"]').text
   try:
      rate = card.find_element(
          By.XPATH, './/span[@class="css-t70v7i"]').text
   except NoSuchElementException:
      rate = "0"
   # count += 1
   titles.append(title)
   prices.append(price)
   rates.append(rate)
   # print(count, "\t", titles, "\t", prices, "\t", rates, "\n")
   # print(count, "\t", titles, "\t", prices, "\n")
sleep(10)
driver.find_element(
    By.XPATH, "//button[@aria-label='Halaman berikutnya']").click()

data['titles'] = titles
data['prices'] = prices
data['rates'] = rates
print(data)

# sellers = driver.find_elements_by_class_name('css-1kdc32b')

# for seller in sellers:
#    print(seller.text)
# items.append(seller.text)
# data['title'] = items

# for title in titles:
#    # print(title.text)
#    items.append(title.text)
# data['title'] = items

# items = []
# for price in prices:
#    # print(price.text)
#    items.append(price.text)
# data['price'] = items

# items = []
# for rate in rates:
#    print(price.text)
#    items.append(rate.text)
# data['rate'] = items

# print(data)
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
# driver.quit()
