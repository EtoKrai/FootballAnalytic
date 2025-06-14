import requests
from bs4 import BeautifulSoup
from io import StringIO
import pandas as pd
import time


def gettable(link):
    headers={"User-Agent": "Mozilla/5.0"}
    response=requests.get(link, headers=headers)
    page=BeautifulSoup(response.text, "html.parser")
    champ=0
    for numb in [9, 12, 20, 13, 11, 37]:
        table_name=f"stats_standard_{numb}"
        if page.find('table', {'id': table_name}) is not None:
            champ=numb
            break
    table_names=[f"stats_keeper_{champ}", f"stats_keeper_adv_{champ}", f"stats_shooting_{champ}", f"stats_passing_{champ}",
                 f"stats_passing_types_{champ}", f"stats_gca_{champ}", f"stats_defense_{champ}", f"stats_possession_{champ}",
                 f"stats_misc_{champ}"]
    i=1
    team=link.split('/')[-1].replace('-Stats-All-Competitions', '').replace('-Stats', '').replace('-', ' ').strip()
    for id in table_names:
        table=page.find('table', {'id': id})
        if table:
            stats=pd.read_html(StringIO(str(table)), header=1)[0]
            stats=stats.drop([stats.index[-1], stats.index[-2]])
            stats=stats.drop(stats.columns[-1], axis=1)
            stats.insert(0, 'Team', team)
            file=f"tables/stats{i}.csv"
            try:
                data=pd.read_csv(file)
                new_data=pd.concat([data, stats]).drop_duplicates()
            except FileNotFoundError:
                new_data=stats
            new_data['Age'] = new_data['Age'].astype(str).str.split('-').str[0]
            new_data['Pos']=new_data['Pos'].replace("MF,FW", "MF")
            new_data['Pos'] = new_data['Pos'].replace("FW,MF", "FW")
            new_data['Pos'] = new_data['Pos'].replace("MF,DF", "MF")
            new_data['Pos'] = new_data['Pos'].replace("DF,MF", "DF")
            new_data['Pos'] = new_data['Pos'].replace("DF,FW", "DF")
            new_data.to_csv(file, index=False)
            i+=1

with open("Leagues/Links.txt") as file:
    for m in file:
        gettable(m)
        time.sleep(1)
