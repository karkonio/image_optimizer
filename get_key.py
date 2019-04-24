from selenium import webdriver
import time
from names import get_first_name
from os import getcwd


options = webdriver.ChromeOptions()
options.binary_location = '/usr/bin/google-chrome-stable'
options.add_argument('--headless')
options.add_argument('--start-maximized')
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
path = getcwd() + '/chromedriver'
driver = webdriver.Chrome(chrome_options=options, executable_path=path)


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
            time.sleep(1)
    print(key.text)
    return key.text
    driver.close()


def confirmation(email):
    registration(email)
    driver.get('https://tempail.com/ru/')
    find_message = False
    while find_message is False:
        try:
            driver.find_element_by_partial_link_text('API').click()
            find_message = True
        except Exception:
            time.sleep(1)
    driver.switch_to.frame(
        driver.find_element_by_id("iframe")
    )
    elems = driver.find_elements_by_xpath("//a[@href]")
    key_is_here = elems[1].get_attribute('href')
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
