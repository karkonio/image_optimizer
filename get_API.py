from requests_html import HTMLSession
import names


session = HTMLSession()


def get_email(session):
    r = session.get('https://temp-mail.org/ru/')
    getmail = r.html.find('#mail.opentip', first=True)
    return getmail.attrs['value']


def registration(session):
    t = session.get('https://tinypng.com/developers')
    random_name = names.get_first_name()
    email = get_email(session)
    inputs = t.html.find(':input')
    print(random_name)
    print(email)
    inputs[0].attrs['required'] = random_name
    inputs[1].attrs['required'] = email
    inputs[2].attrs['autocomplete'] = 'on'


registration(session)
