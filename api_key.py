from selenium import webdriver
import time
import names
# from bs4 import BeautifulSoup
# import requests


driver = webdriver.Chrome('/home/korka/Roborin/image_optimizer/chromedriver')


def get_email(url1):
    driver.get(url1)
    email = driver.find_element_by_css_selector('input[id="eposta_adres"]').\
        get_attribute('data-clipboard-text')
    return email


# headless
def api():
    email = get_email('https://tempail.com/ru/')
    key_is_here = confirmation(email)
    driver.get(key_is_here)
    time.sleep(2)
    a = driver.find_element_by_css_selector('body > div:nth-child(2) > div > main:nth-child(1) > section > div > table > tbody > tr.requested > td.key > span')
    print(a.text)
    return a.text


def confirmation(email):
    registration(email)
    driver.get('https://tempail.com/ru/')
    time.sleep(10)
    driver.find_element_by_partial_link_text('API').click()
    driver.switch_to.frame(
        driver.find_element_by_id("iframe")
    )
    elems = driver.find_elements_by_xpath("//a[@href]")
    key_is_here = elems[1].get_attribute('href')
    return key_is_here


def registration(email):
    random_name = names.get_first_name()
    print(random_name)
    print(email)
    driver.get('https://tinypng.com/developers')
    driver.find_element_by_css_selector('input[name="fullName"]').\
        send_keys(random_name)
    driver.find_element_by_css_selector('input[name="mail"]').send_keys(email)
    driver.find_element_by_css_selector('input[type=submit]').click()


if __name__ == '__main__':
    api()
