from requests_html import HTMLSession
from selenium import webdriver
import time
import names


url_1 = 'https://temp-mail.org/ru/'
url_2 = 'https://tinypng.com/developers'
el_1 = 'input[name="fullName"]'
el_2 = 'input[name="mail"]'
el_3 = 'input[type=submit]'
el_4 = 'API'
el_5 = '/html/body/div[1]/div/div/div[2]/div[1]/div[1]/div[3]/div/div/table/tbody/tr/td/table/tbody/tr[3]/td[2]/p[3]/a'
el_6 = 'mail'
el_7 = 'value'
driver = webdriver.Chrome('/home/kumir/environments/temp_tiny/chromedriver')
session = HTMLSession()


def tiny_registration():
    user_name = names.get_first_name()
    email = driver.find_element_by_id(el_6).get_attribute(el_7)
    driver.get(url_2)
    driver.find_element_by_css_selector(el_1).send_keys(user_name)
    driver.find_element_by_css_selector(el_2).send_keys(email)
    driver.find_element_by_css_selector(el_3).click()


def get_api_from_mail():
    driver.get(url_1)
    tiny_registration()
    driver.get(url_1)
    time.sleep(15)
    driver.find_element_by_partial_link_text(el_4).click()
    time.sleep(5)
    button = driver.find_elements_by_xpath(el_5)
    button[0].click()


if __name__ == '__main__':
    get_api_from_mail()