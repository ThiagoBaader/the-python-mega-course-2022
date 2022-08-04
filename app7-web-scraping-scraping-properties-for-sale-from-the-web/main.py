# library import
import requests
from bs4 import BeautifulSoup
import pandas

base_url = "https://pythonizing.github.io/data/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="

# list to store the dictionaries
l = []

# loading the webpage
r = requests.get("https://pythonizing.github.io/data/real-estate/rock-springs-wy/LCWYROCKSPRINGS/")
c = r.content
soup = BeautifulSoup(c, "html.parser")

# discover the number of pages in the website
page_nr = soup.find_all("a", {"class": "Page"})[-1].text

# crawling through multiple web pages
for page in range(0,int(page_nr) * 10,10):  # page_nr * 10 because the pattern of the website, where page 1 = 0, page 2 = 10, page 3 = 20, ... 
    # loading the webpage
    r = requests.get(base_url + str(page) + ".html")
    c = r.content
    soup = BeautifulSoup(c, "html.parser")

    # extracting div elements
    all = soup.find_all("div", {"class": "propertyRow"})

    # scraping the adresses of the properties
    for item in all:
        d ={}
        d["Address"] = item.find_all("span", {"class", "propAddressCollapse"})[0].text
        d["Locality"] = item.find_all("span", {"class", "propAddressCollapse"})[1].text
        d["Price"] = item.find("h4", {"class", "propPrice"}).text.replace("\n", "").replace(" ", "")
        try:
            d["Beds"] = item.find("span", {"class", "infoBed"}).find("b").text
        except:
            d["Beds"] = None
        try:
            d["Area"] = item.find("span", {"class", "infoSqFt"}).find("b").text
        except:
            d["Area"] = None
        try:
            d["Full Baths"] = item.find("span", {"class", "infoValueFullBath"}).find("b").text
        except:
            d["Full Baths"] = None
        try:
            d["Half Baths"] = item.find("span", {"class", "infoValueHalfBath"}).find("b").text
        except:
            d["Half Baths"] = None

        # scraping especial elements
        for column_group in item.find_all("div", {"class", "columnGroup"}):
            for feature_group, feature_name in zip(column_group.find_all("span", {"class": "featureGroup"}), column_group.find_all("span", {"class": "featureName"})):
                if "Lot Size" in feature_group.text:
                    d["Lot Size"] = feature_name.text
        l.append(d)

# saving the extracted data in csv files
df = pandas.DataFrame(l)
df.to_csv("Output.csv")
