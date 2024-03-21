import pandas as pd
import numpy as np
import csv
import web_driver as wd
import site_crawler as sc
import os
import glob



def grab_data(years):
    # Goes through each year and grabs teams and links

    for year, link in years.items():
        dic = sc.get_team_sites(link["Overview"], year)
        years[year]["Teams"] = dic
    return years


def player_db(all_clubs):
    all_players = pd.read_csv("players.csv").to_dict()
    for year in all_clubs:
        for team in all_clubs[year]["Teams"]:
            all_players = sc.get_all_players(all_clubs[year]["Teams"][team], all_players)
            pd.DataFrame(all_players.items()).to_csv("players.csv")
    return all_players


def team_stats(teams):
    for team in teams.iloc[:,-1]:
        sc.get_player_stats(team)

def reform(files):
    for f in files:
        table = pd.read_csv(file, encoding="utf-32")
        table.iloc[:2,:].to_csv("asdf.csv")


def main():
    # Initializes the years we want to grab data from
    years = {"17-18": {"Overview":"https://fbref.com/en/comps/9/2017-2018/2017-2018-Premier-League-Stats"},
             "18-19": {"Overview":"https://fbref.com/en/comps/9/2018-2019/2018-2019-Premier-League-Stats"},
             "19-20": {"Overview":"https://fbref.com/en/comps/9/2019-2020/2019-2020-Premier-League-Stats"},
             "20-21": {"Overview":"https://fbref.com/en/comps/9/2020-2021/2020-2021-Premier-League-Stats"},
             "21-22": {"Overview":"https://fbref.com/en/comps/9/2021-2022/2021-2022-Premier-League-Stats"},
             "22-23": {"Overview":"https://fbref.com/en/comps/9/2022-2023/2022-2023-Premier-League-Stats"}}

    
    # file = "player_data" + os.sep + "2017-2018" + os.sep + "Arsenal" + os.sep + "standard.csv"
    # table = pd.read_csv(file, encoding="utf-32").iloc[:-2,:]
    # table.to_csv("asdf.csv", encoding="utf-32")

    # filepaths = glob.glob("player_data/*/*/*")
    # print(table)


    # sc.f_path("https://fbref.com/en/squads/8602292d/2022-2023/Aston-Villa-Stats")

    # sc.get_player_stats("https://fbref.com/en/squads/8602292d/2022-2023/Aston-Villa-Stats")
    # av_data.to_csv("dataframe.csv")
    # print(av_data)


main()
