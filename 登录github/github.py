#coding=utf-8
import requests
from bs4 import BeautifulSoup

login_url = 'https://github.com/login'
session_url = 'https://github.com/session'

s = requests.session()
r = s.get(login_url)
html = r.text
soup = BeautifulSoup(html,'html.parser')
authenticity_token = soup.find(
    'input',{'name':'authenticity_token'}).get('value')

data = {
    'commit':'Sign in',
    'utf8':'✓',
    'authenticity_token':authenticity_token,
    'login':' ',
    'password':' '
}

r = s.post(session_url,data=data)

html = r.text
soup = BeautifulSoup(html,'html.parser')
repo = soup.find_all('span','css-truncate css-truncate-target')
for i in repo:
    print(i.get('title'))
