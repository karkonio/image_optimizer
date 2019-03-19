from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from time import sleep
from names import get_first_name
from os import getcwd


options = Options()
options.headless = True
path = getcwd() + '/chromedriver'
driver = webdriver.Chrome(path, chrome_options=options)


def get_email(url1):
    driver.get(url1)
    email = driver.find_element_by_css_selector('input[id="eposta_adres"]').\
        get_attribute('data-clipboard-text')
    return email


def api():
    email = get_email('https://tempail.com/ru/')
    key_url = confirmation(email)
    driver.get(key_url)
    find_key = False
    while find_key is False:
        try:
            key = driver.find_element_by_css_selector('body > div:nth-child(2) > div\
                 > main:nth-child(1) > section > div > table > tbody \
                 > tr.requested > td.key > span')
            find_key = True
        except Exception:
            sleep(1)
    print(key.text)
    return key.text


def confirmation(email):
    registration(email)
    driver.get('https://tempail.com/ru/')
    find_message = False
    while find_message is False:
        try:
            driver.find_element_by_partial_link_text('API').click()
            driver.switch_to.frame(
                driver.find_element_by_id("iframe")
            )
            elems = driver.find_elements_by_xpath("//a[@href]")
            key_is_here = elems[1].get_attribute('href')
            find_message = True
        except Exception:
            sleep(1)
    return key_is_here


def registration(email):
    random_name = get_first_name()
    driver.get('https://tinypng.com/developers')
    driver.find_element_by_css_selector('input[name="fullName"]').\
        send_keys(random_name)
    driver.find_element_by_css_selector('input[name="mail"]').send_keys(email)
    driver.find_element_by_css_selector('input[type=submit]').click()


if __name__ == '__main__':
    api()
