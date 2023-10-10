#Python libraries:
import pandas as pd
from bs4 import BeautifulSoup
import requests
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# Data taken from the website:
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/117.0.0.0 Safari/537.36 OPR/103.0.0.0'
}
url = "https://www.pamatyklietuvoje.lt/keliones/marsrutai-pesciomis/10"
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
forecast = soup.find_all("div", class_="col-xs-12 col-sm-6 col-lg-4")
print(forecast)
RoutesOnFoot = []
for routes in forecast:
    title = routes.find_all("div", class_="trip-title").text.strip()
    distance = routes.find("span", class_="pl pl-distance").text.strip()
    duration = routes.find("span", class_="pl pl-duration").text.strip()
    objects = routes.find("span", class_="pl pl-poi").text.strip()
    RoutesOnFoot.append((title, distance, duration, objects))
    df = pd.DataFrame(RoutesOnFoot, columns=["Title", "Distance", "Duration", "Objects"])
    print(df)

