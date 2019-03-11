from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
import names
from os import getcwd


options = Options()
options.headless = True
path = getcwd() + '/chromedriver'
driver = webdriver.Chrome(path, chrome_options=options)


def get_email(url):
    driver.get(url)
    email = driver.find_element_by_css_selector('input[id="mail"]').\
        get_attribute('value')
    return email


def api():
    email = get_email('https://temp-mail.org/')
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
            time.sleep(0.5)
    return key.text


def confirmation(email):
    registration(email)
    driver.get('https://temp-mail.org/')
    print(email)
    find_message = False
    while find_message is False:
        try:
            driver.find_element_by_css_selector('a.title-subject').click()
            find_message = True
        except Exception:
            time.sleep(0.5)
    time.sleep(0.5)
    elem = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[1]/\
        div[1]/div[3]/div/div/table/tbody/tr/td/table/\
        tbody/tr[3]/td[2]/p[3]/a')
    key_is_here = elem.get_attribute('href')
    return key_is_here


def registration(email):
    random_name = names.get_first_name()
    driver.get('https://tinypng.com/developers')
    driver.find_element_by_css_selector('input[name="fullName"]').\
        send_keys(random_name)
    driver.find_element_by_css_selector('input[name="mail"]').send_keys(email)
    driver.find_element_by_css_selector('input[type=submit]').click()


if __name__ == '__main__':
    api()
    # get_api_from_mail()
