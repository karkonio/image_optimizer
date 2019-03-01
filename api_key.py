from requests_html import HTMLSession
from selenium import webdriver
import time
import names

session = HTMLSession()
driver = webdriver.Chrome('/home/korka/Roborin/image_optimizer/chromedriver')


def get_email():
    email = driver.find_element_by_id('eposta_adres').\
        get_attribute('data-clipboard-text')
    return email


def registration():
    random_name = names.get_first_name()
    email = get_email()
    print(random_name)
    print(email)
    url = 'https://tinypng.com/developers'
    driver.get(url)
    driver.find_element_by_css_selector('input[name="fullName"]').\
        send_keys(random_name)
    driver.find_element_by_css_selector('input[name="mail"]').send_keys(email)
    driver.find_element_by_css_selector('input[type=submit]').click()


def confirmation():
    # url = 'https://temp-mail.org/ru/'
    driver.get('https://tempail.com/ru/')
    registration()
    driver.get('https://tempail.com/ru/')
    time.sleep(11)
    driver.find_element_by_partial_link_text('API').click()
    time.sleep(2)
    print('press')
    driver.switch_to.frame(
        driver.find_element_by_id("iframe")
    )
    elems = driver.find_elements_by_xpath("//a[@href]")
    elems[1].click()


if __name__ == '__main__':
    confirmation()
