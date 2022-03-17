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
   header = ['titles', 'prices', 'rates']
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
      y += 600
      sleep(2)

   # titles, prices, rates = [], [], []
   # data = pd.DataFrame()

   # catalog = driver.find_element(
   #    By.XPATH, '//div[@data-testid="divSRPContentProducts"]')
   # container = catalog.find_elements(
   #    By.XPATH, './/div[@class="css-jza1fo"]')
   cards = driver.find_elements(
       By.XPATH, './/div[@class="css-12sieg3"]')
   return cards
   # print("Total container : ", len(container))
   # print("Total cards : ", len(cards))
   # driver.find_element(
   #    By.XPATH, '//div[@class="unf-coachmark__next-button css-64apm5 e1o9jid35"]').click()


# count = 0
# for card in cards:
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
   # count += 1
   product = (title, price, rate)
   return product

   # titles.append(title)
   # prices.append(price)
   # rates.append(rate)
   # print(count, "\t", titles, "\t", prices, "\t", rates, "\n")
   # print(count, "\t", titles, "\t", prices, "\n")
# sleep(10)

# data['titles'] = titles
# data['prices'] = prices
# data['rates'] = rates
# print(data)


def main(search_term, pages, filepath):
   driver = create_webdriver_instance()
   save_tweet_data_to_csv(None, filepath, 'w')
   query_search(driver, search_term)
   for i in range(pages):
      if i == 0:
         driver.find_element(
             By.XPATH, '//div[@class="unf-coachmark__next-button css-64apm5 e1o9jid35"]').click()

      cards = load_catalog(driver)
      count = 0
      for card in cards:
         product = extract_from_card(card)
         save_tweet_data_to_csv(product, filepath)
         count += 1
         print(count)

      # driver.find_element(
      #     By.XPATH, "//button[@aria-label='Halaman berikutnya']").click()
      find_next_button(driver)


if __name__ == '__main__':
   term = 'iphone'
   path = term + '.txt'
   pages = 4

   main(term, pages, path)
