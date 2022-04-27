from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
import csv
# import pandas as pd


def create_webdriver_instance():
   driver = Chrome()
   return driver


def query_search(driver, search_term):
   url = 'https://www.tokopedia.com/'
   # search_term = 'huawei'
   driver.get(url)

   search_input = driver.find_element(
       By.XPATH, '//input[@aria-label="Bidang pencarian"]')
   search_input.send_keys(search_term)
   search_input.send_keys(Keys.RETURN)
   sleep(5)


def save_tweet_data_to_csv(records, filepath, mode='a+'):
   header = ['Subjek', 'Harga', 'Rating', 'Penjual', 'Asal', 'url']
   with open(filepath, mode=mode, newline='', encoding='utf-8') as f:
      writer = csv.writer(f, delimiter='\t')
      if mode == 'w':
         writer.writerow(header)
      if records:
         writer.writerow(records)


def find_next_button(driver):
   element = driver.find_element(
       By.XPATH, "//button[@aria-label='Halaman berikutnya']")
   desired_y = (element.size['height'] / 2) + element.location['y']
   current_y = (driver.execute_script('return window.innerHeight') /
                2) + driver.execute_script('return window.pageYOffset')
   scroll_y_by = desired_y - current_y
   driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)
   driver.find_element(
       By.XPATH, "//button[@aria-label='Halaman berikutnya']").click()


def load_catalog(driver):
   # scroll
   y = 1000
   for timer in range(0, 9):
      driver.execute_script("window.scrollTo(0, "+str(y)+")")
      y += 800
      sleep(2)

   cards = driver.find_elements(
       By.XPATH, './/div[@class="css-12sieg3"]')
   return cards


def extract_from_card(card):
   title = card.find_element(
       By.XPATH, './/div[@class="css-1b6t4dn"]').text
   price = card.find_element(
       By.XPATH, './/div[@class="css-1ksb19c"]').text
   try:
      rate = card.find_element(
          By.XPATH, './/span[@class="css-t70v7i"]').text
   except NoSuchElementException:
      rate = "0"
   sellers = card.find_elements_by_class_name('css-1kdc32b')
   count = 0
   for seller in sellers:
      if count == 0:
         seller_town = seller.text
      else:
         seller_user = seller.text
      count += 1
   seller_url = card.find_element(
       By.XPATH, './/div[@class="css-974ipl"]/a').get_attribute('href')
   # seller_url = "no_url"
   product = (title, price, rate, seller_user, seller_town, seller_url)
   return product


def main(search_term, pages, filepath):
   driver = create_webdriver_instance()
   save_tweet_data_to_csv(None, filepath, 'w')
   query_search(driver, search_term)
   count = 0
   for i in range(pages):
      
      # pop up click
      if i == 0:
         driver.find_element(
             By.XPATH, '//div[@class="unf-coachmark__next-button css-64apm5 e1o9jid35"]').click()

      cards = load_catalog(driver)
      for card in cards:
         product = extract_from_card(card)
         save_tweet_data_to_csv(product, filepath)
         count += 1
         print((i+1), "-", count)

      if i == pages:
         break
      find_next_button(driver)


if __name__ == '__main__':
   term = input("Search Term : ")
   path = term + '.txt'
   pages = 2

   main(term, pages, path)
