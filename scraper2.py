import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
START_URL = "https://exoplanets.nasa.gov/exoplanet/catalog/"
browser = webdriver.Chrome('/Users/approve/Downloads/chromedriver')
browser.get(START_URL)
time.sleep(10)
headers = ["name","light_years_from_earth","planet_mass","stellar_magnitude","discovery_date","hyper_link"]
planet_data = []
def scrape_more_data(hyper_link):
    pass
scrape()
for data in planet_data:
    scrape_more_data(data[5])
page = requests.get(hyperlink)
soup = BeautifulSoup(page.content,"html.parser")
def scrape_more_data(hyperlink):
    page = requests.get(hyperlink)
    soup = BeautifulSoup(page.content,"html.parser")
    for tr_tag in soup.find_all("tr",attrs = {"class":"fact_row"} ):
        td_tags = tr_tag.find_all("td")
        temp_list = []
        for td_tag in td_tags:
            try:
                temp_list.append(td_tag.find_all("div",attrs = {"class":"value"})[0].contents[0])
            except:
                temp_list.append("")
        new_planet_data.append(temp_list)
final_planet_data=[]
for index,data in enumerate(planet_data):
    final_planet_data.append(data+final_planet_data[index])
with open("final.csv", "w") as f:
    csvwriter = csv.writer()
    csvwriter.writerow(headers)
    csvwriter.writerows(final_planet_data)