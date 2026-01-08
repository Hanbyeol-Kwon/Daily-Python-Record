import urllib.request

url = "https://www.naver.com"

res = urllib.request.urlopen(url)
data = res.read()
text = data.decode("utf-8")

print(text)

