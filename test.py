#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    
    # Hello there

    print("Testing VS Code.")

    my_file = open("init_data_extract.txt", "w")

    url = "https://visiteasterncape.co.za/iconic-eastern-cape/"
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")

    print()
    #region_heading = soup.find('h3', class_='elementor-heading-title elementor-size-default')
    #my_file.write(region_heading.string)
    print()

    my_file.close()

    a_file = open("init_data_extract.txt", "a")

    regions_sa = soup.find('div', class_='elementor-column elementor-col-50 elementor-inner-column elementor-element elementor-element-7579cdf')
    for regionsa in regions_sa:
        #print(regionsa.get_text())
        #a_file.write(regionsa.text)
        a_file.write(regionsa.text)
    
    a_file.close()

    finalfile = open("some_data.txt", "w+")

    with open("init_data_extract.txt", "r+") as dafile:
        for line in dafile:
            if not line.isspace():
                finalfile.write(line) 
            
    dafile.close()
    finalfile.close()
    
    diefile = open("requirements.txt", "w")
    diefile.write("beautifulsoup4\n")
    diefile.write("requests\n")
    diefile.close()

    the_file = open("some_data.txt", "r")
    for row in the_file:
        print(row) 
    the_file.close()

    # print(page.text)



