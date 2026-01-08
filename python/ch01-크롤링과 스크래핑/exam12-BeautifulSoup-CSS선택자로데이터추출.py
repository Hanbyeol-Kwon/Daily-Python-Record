from bs4 import BeautifulSoup

fp = open("fruits-vegetables.html", encoding="utf-8")
soup = BeautifulSoup(fp, "html.parser")

print(soup.select_one("li:first-child").string)
print(soup.select_one("#fr-list > li:nth-child(4)").string)
print(soup.select("#ve-list > li[data-lo='us']")[1].string)
print(soup.select("#ve-list > li.black")[1].string)

cond = {"data-lo":"ko", "class":"black"}
print(soup.find("li", cond).string)
print(soup.find(id="ve-list").find("li", cond).string)






















