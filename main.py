import pandas as pd
import numpy as np
import csv
import web_driver as wd
import site_crawler as sc



def grab_data(years):
    # Goes through each year and grabs teams and links

    for year, link in years.items():
        dic = sc.get_team_sites(link["Overview"], year)
        years[year]["Teams"] = dic
    return years


def player_db(all_clubs):
    all_players = dict()
    found = []
    for year in all_clubs:
        for team in all_clubs[year]["Teams"]:
            club_team, listy = sc.get_all_players(all_clubs[year]["Teams"][team], found)
            all_players |= club_team
            found = listy
    return all_players

def main():
    # Initializes the years we want to grab data from
    years = {"17-18": {"Overview":"https://fbref.com/en/comps/9/2017-2018/2017-2018-Premier-League-Stats"},
             "18-19": {"Overview":"https://fbref.com/en/comps/9/2018-2019/2018-2019-Premier-League-Stats"},
             "19-20": {"Overview":"https://fbref.com/en/comps/9/2019-2020/2019-2020-Premier-League-Stats"},
             "20-21": {"Overview":"https://fbref.com/en/comps/9/2020-2021/2020-2021-Premier-League-Stats"},
             "21-22": {"Overview":"https://fbref.com/en/comps/9/2021-2022/2021-2022-Premier-League-Stats"},
             "22-23": {"Overview":"https://fbref.com/en/comps/9/2022-2023/2022-2023-Premier-League-Stats"}}

    test = {"17-18": {"Overview":"https://fbref.com/en/comps/9/2017-2018/2017-2018-Premier-League-Stats"}}
    test2 = {"17-18": {"Overview":"https://fbref.com/en/comps/9/2017-2018/2017-2018-Premier-League-Stats", "Teams":{"Manchester City":"https://fbref.com/en/squads/b8fd03ef/2018-2019/Manchester-City-Stats", "Manchester C": "https://fbref.com/en/squads/b8fd03ef/2017-2018/Manchester-City-Stats"}}}

    # ap = player_db(grab_data(test))
    # pd.DataFrame(ap.items()).to_csv("players.csv")

    aa = player_db(test2)
    pd.DataFrame(aa.items()).to_csv("players_test.csv")

    # clubs_data = grab_data(years)
    # print(clubs_data)

    # print(player_db(grab_data(test)))

    # av_data = sc.get_player_stats("https://fbref.com/en/squads/8602292d/2022-2023/Aston-Villa-Stats")
    # av_data.to_csv("dataframe.csv")
    # print(av_data)

    # hello = sc.get_all_players("https://fbref.com/en/squads/8602292d/2022-2023/Aston-Villa-Stats")
    # print(hello)

    # sc.get_player_tm('https://fbref.com/en/players/819b3158/Ilkay-Gundogan')

main()
