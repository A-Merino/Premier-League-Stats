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
        with open(f, "r", encoding="utf-32") as g:
            for line in g:
                print(line)
        # t = f.split("\\")[-1]
        # print(t)
        # table = pd.read_csv(f, encoding="latin", sep=",")
        # table.iloc[:-2,:].to_csv(f, sep=",")



def combtable(folder, file):
    # folder = folder[1:]
    players = []
    for f in reversed(folder):
        print(f)
        try:
            one = pd.read_csv(f, on_bad_lines='skip')
        except Exception as e:
            one = pd.read_csv(f, encoding="latin", on_bad_lines='skip')
        else:
            pass
        finally:
            pass
            # print(one)
        for i in range(one.shape[0]):
            
            players.append(list(one.iloc[i,:].values))


    pd.DataFrame.from_records(players).to_csv(file +"/all.csv")


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
    rf = "player_data/allteams/"
    filepaths = glob.glob("player_data/*/*/all.csv")
    for file in filepaths:
        # subs = glob.glob(file + "/*")
        out = file.split("\\")[2] + file.split("\\")[1] + file[-4:]
        # combtable(subs, file)
        # for s in subs:
        #     print(s)
        os.rename(file, rf + out)
        print(file)

    # reform(glob.glob("player_data/2021-2022/Southampton/*"))

    # sc.f_path("https://fbref.com/en/squads/8602292d/2022-2023/Aston-Villa-Stats")

    # sc.get_player_stats("https://fbref.com/en/squads/8602292d/2022-2023/Aston-Villa-Stats")
    # av_data.to_csv("dataframe.csv")
    # print(av_data)


main()
