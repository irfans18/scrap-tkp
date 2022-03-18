# import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By

search_term = input("Masukan keyword : ")

driver = Chrome()
driver.implicitly_wait(10)

url = 'https://www.tokopedia.com/'
driver.get(url)

search_input = driver.find_element_by_xpath(
    '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[1]/input[1]')
search_input.send_keys(search_term)
search_input.send_keys(Keys.RETURN)
sleep(5)

# close popup
driver.find_element(
    By.XPATH, '//div[@class="unf-coachmark__next-button css-64apm5 e1o9jid35"]').click()

# this scrolls untill the element is in the middle of the page
# for i in range(10):
# y = 1000
# for timer in range(0, 9):
#    driver.execute_script("window.scrollTo(0, "+str(y)+")")
#    y += 600
#    sleep(1)
# scroll
# element = driver.find_element(
#     By.XPATH, "//button[@aria-label='Halaman berikutnya']")
# desired_y = (element.size['height'] / 2) + element.location['y']
# current_y = (driver.execute_script('return window.innerHeight') /
#              2) + driver.execute_script('return window.pageYOffset')
# scroll_y_by = desired_y - current_y
# driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)
# driver.find_element(
#     By.XPATH, "//button[@aria-label='Halaman berikutnya']").click()

cards = driver.find_elements(
    By.XPATH, './/div[@class="css-12sieg3"]')
count = 0
for card in cards:
   count += 1
   # i = card.find_elements(By.XPATH,
   #                       '//span[@class="css-1kdc32b"]').text
   sellers = card.find_elements_by_class_name('css-1kdc32b')
   for seller in sellers:
      print(count, "-", seller.text)
   toko_url = card.find_element(
       By.XPATH, './/div[@class="css-zimbi"]/a').get_attribute('href')
   # toko_url = card.find_element(
   #     By.XPATH, '//*[@id="2283016203"]/div/div/div/div/div[1]/a').text
   # print(count, "-", toko_url)
# //*[@id="2283016203"]/div/div/div/div/div[1]/a
