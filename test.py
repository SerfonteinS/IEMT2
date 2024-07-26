# Hello there

print("Testing VS Code.")

import requests
from bs4 import BeautifulSoup

url = "https://visiteasterncape.co.za/iconic-eastern-cape/"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

print()
region_heading = soup.find('h3', class_='elementor-heading-title elementor-size-default')
print(region_heading.get_text())
print()

regions_sa = soup.find('div', class_='elementor-column elementor-col-50 elementor-inner-column elementor-element elementor-element-7579cdf')
for regionsa in regions_sa:
    print(regionsa.get_text())

# print(page.text)



