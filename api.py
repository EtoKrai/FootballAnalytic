import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://fbref.com/en/squads/b8fd03ef/Manchester-City-Stats"
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)
test = BeautifulSoup(response.text, "html.parser")
stats = test.find("table", {"id": "stats_standard_9"})
if stats:
    df = pd.read_html(str(stats))[0]
    df.to_csv("mancity_stats.csv", index=False)
else:
    print("Fail")
