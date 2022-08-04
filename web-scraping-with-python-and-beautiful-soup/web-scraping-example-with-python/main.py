import requests
from bs4 import BeautifulSoup

r = requests.get("https://pythonizing.github.io/data/example.html")
c = r.content

soup = BeautifulSoup(c, "html.parser")

all = soup.find_all("div", {"class":"cities"})

for item in all:
    print(item.find_all("h2")[0].text)
