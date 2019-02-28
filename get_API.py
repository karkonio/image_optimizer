from requests_html import HTMLSession
import names


session = HTMLSession()


def get_email(session):
    r = session.get('https://temp-mail.org/ru/')
    getmail = r.html.find('#mail.opentip', first=True)
    return getmail.attrs['value']


def registration(session):
    t = session.get('https://tinypng.com/developers')
    name = t.html.find('#Your full name', first=True)
    email = t.html.find('#Your email address', first=True)
    submit = t.html.find('#submit', first=True)
    random_name = names.get_first_name()
    email = get_email()
    name.attrs['name'] = random_name
    email.attrs['name'] = email
    submit.attrs['autocomplete'] = 'on'
