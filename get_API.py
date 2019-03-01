from requests_html import HTMLSession
from selenium import webdriver
import time
import names

session = HTMLSession()
driver = webdriver.Chrome('/home/korka/Roborin/image_optimizer/chromedriver')
driver.get('https://temp-mail.org/ru/')
# r = session.get('https://temp-mail.org/ru/')
# url = 'https://temp-mail.org/ru/'


def get_email():
    return driver.find_element_by_id('mail').get_attribute('value')
    # r = session.get(url)
    # getmail = r.html.find('#mail.opentip', first=True)
    # return getmail.attrs['value']


def registration():
    random_name = names.get_first_name()
    email = get_email()
    print(random_name)
    print(email)
    url = 'https://tinypng.com/developers'
    driver.get(url)
    # email = driver.find_element_by_id('mail').get_attribute('value')
    print('OKKK, bari ok')
    driver.find_element_by_css_selector('input[name="fullName"]').\
        send_keys(random_name)
    driver.find_element_by_css_selector('input[name="mail"]').send_keys(email)
    driver.find_element_by_css_selector('input[type=submit]').click()


def confirmation():
    # url = 'https://temp-mail.org/ru/'
    print(2)
    driver.get('https://temp-mail.org/ru/')
    print(777)
    registration()
    print(763425)
    driver.get('https://temp-mail.org/ru/')
    driver.find_element_by_id('click-to-refresh').click()
    time.sleep(10)
    driver.find_element_by_class_name('title-subject').click()
    time.sleep(5)
    driver.find_element_by_partial_link_text('Visit').click()


if __name__ == '__main__':
    print('stsrt')
    # get_email()
    # registration()
    print('stsrt')
    confirmation()
