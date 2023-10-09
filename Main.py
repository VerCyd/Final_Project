#Python libraries:
import pandas as pd
from bs4 import BeautifulSoup
import requests
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


#Data taken from the website:
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/117.0.0.0 Safari/537.36 OPR/102.0.0.0'
}
for i in range(1, 12):
    url = "https://www.pamatyklietuvoje.lt/zemelapis?scf=1%2C2&xmax=283228&xmin=11.2720&ymax=" \
          f"59.4339&ymin=49.8805&stf=37{i}"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    forecast = soup.find_all("div", class_ = "resultItem")
    print(forecast)
    PlacesToVisit = []
    for places in forecast:
        title = places.find("div", class_ = "detailsContainer").text.strip()
        species = places.find("div", class_ = "resultItem_subTypeText").text.strip()
        address = places.find("div", class_ = "resultItem_addressText").text.strip()
        PlacesToVisit.append((title, species, address))
    df = pd.DataFrame(PlacesToVisit, columns = ["Title", "Species", "Address"])
    print(df)




