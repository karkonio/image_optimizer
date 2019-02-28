from requests_html import HTMLSession
from selenium import webdriver
import names

session = HTMLSession()
driver = webdriver.Chrome('/home/korka/Roborin/image_optimizer/chromedriver')
r = session.get('https://temp-mail.org/ru/')
url = 'https://temp-mail.org/ru/'


def get_email(url):
    r = session.get(url)
    getmail = r.html.find('#mail.opentip', first=True)
    return getmail.attrs['value']


def registration():
    url = 'https://tinypng.com/developers'
    driver.get(url)
    random_name = names.get_first_name()
    email = get_email(url)
    print(random_name)
    print(email)
    driver.find_element_by_css_selector('input[name="fullName"]').\
        send_keys(random_name)
    driver.find_element_by_css_selector('input[name="mail"]').send_keys(email)
    driver.find_element_by_css_selector('input[type=submit]').click()


def confirmation(url):
    driver.get(url)
    registration()
    driver.find_element_by_class_name('title-subject').click()
    driver.find_element_by_css_selector('input[target="_blank"]').click()
    pass


if __name__ == '__main__':
    confirmation(url)
