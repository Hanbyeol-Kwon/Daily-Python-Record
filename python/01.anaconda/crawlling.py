# import requests
# from bs4 import BeautifulSoup
# info = requests.get('http://v.media.daum.net/v/20170615203441266')
# soup = BeautifulSoup(info.content, 'html.parser')
# owndata=soup.find('title')
# print(soup)

from bs4 import BeautifulSoup
html = '''<html>
            <body>
                <h1 id='title'>[1]크롤링이란?</h1>
                <p class='cssstyle'>웹페이지에서 필요한 데이터를 추출하는 것</p>
                <p id='body' align='center'>파이썬을 중심으로 다양한 웹크롤링 기술 발달</p>
            </body>
        </html>'''
soup = BeautifulSoup(html, "html.parser")
# 태그로 검색 방법
data = soup.find(id='body')
print(data) 
print(data.string) #텍스트만 출력 방법 1
print(data.get_text()) #텍스트만 출력 방법 2 