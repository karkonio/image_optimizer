from requests_html import HTMLSession
from selenium import webdriver
import time
import names


driver = webdriver.Chrome('/home/kumir/environments/temp_tiny/chromedriver')
session = HTMLSession()
url_1 = 'https://tempail.com/ru/'
url_2 = 'https://tinypng.com/developers'
el_1 = 'input[id="eposta_adres"]'
el_2 = 'data-clipboard-text'
el_3 = 'body > div:nth-child(2) > div > main:nth-child(1) > section > div > table > tbody > tr.requested > td.key > span'
el_4 = 'API'
el_5 = 'iframe'
el_6 = '//a[@href]'
el_7 = 'href'
el_8 = 'input[name="fullName"]'
el_9 = 'input[name="mail"]'
el_10 = 'input[type=submit]'


def get_email(url1):
    driver.get(url1)
    email = driver.find_element_by_css_selector(el_1).get_attribute(el_2)
    return email


def get_api():
    email = get_email(url_1)
    key_url = confirmation(email)
    driver.get(key_url)
    time.sleep(2)
    api = driver.find_element_by_css_selector(el_3)
    print(api.text)
    return api.text


def confirmation(email):
    tiny_registration(email)
    driver.get(url_1)
    time.sleep(10)
    driver.find_element_by_partial_link_text(el_4).click()
    driver.switch_to.frame(driver.find_element_by_id(el_5))
    elems = driver.find_elements_by_xpath(el_6)
    key_url = elems[1].get_attribute(el_7)
    return key_url


def tiny_registration(email):
    user_name = names.get_first_name()
    print(user_name)
    print(email)
    driver.get(url_2)
    driver.find_element_by_css_selector(el_8).send_keys(user_name)
    driver.find_element_by_css_selector(el_9).send_keys(email)
    driver.find_element_by_css_selector(el_10).click()


if __name__ == '__main__':
    get_api()

