import requests
from bs4 import Beautifulsoup
info = requests.get('http://v.media.daum.net/v/20170615203441266')
soup = Beautifulsoup(info.content, 'html.parser')
owndata=soup.find('title')
print(owndata.get_text())