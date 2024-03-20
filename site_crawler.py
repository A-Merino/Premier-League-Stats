import web_driver as wd
import tables as tb
import pandas as pd
import numpy as np
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import os
import glob


def get_team_sites(url, year):
    links = dict()
    # Each season requires a unique table id
    f, s = year.split('-')  
    ids = "".join(("results20", f, "-20", s, "91_overall"))

    # Create web driver and find season table
    d = wd.init_loaded_page_id(url, ids)
    table = d.find_element(By.ID, ids)
    bod = table.find_element(By.CSS_SELECTOR, "tbody")
    trs = bod.find_elements(By.CSS_SELECTOR, "tr")

    # Find club name and link to that season's player stats
    for row in trs:
        o = row.find_element(By.CSS_SELECTOR, "a")
        links[o.text] = o.get_attribute("href") 

    # Close web driver and return dict of clubs
    d.close()
    return links


def get_player_stats(url):
    dest = f_path(url)
    players = dict()
    tables = ["stats_standard_9", "stats_shooting_9", "stats_passing_9",
            "stats_passing_types_9", "stats_gca_9", "stats_defense_9",
            "stats_possession_9", "stats_playing_time_9", "stats_misc_9",
            "stats_keeper_9", "stats_keeper_adv_9"]
    d = wd.init_loaded_page_id(url, "stats_misc_9")
    club_stats = pd.DataFrame()
    for tab in tables:
        tb.table_cleaner(d.find_element(By.ID, tab).text, dest, tab.split("_")[-2])
        # club_stats = tb.table_joiner(club_stats)
    d.close()
    # return club_stats


def f_path(url):
    year, team = url.split("/")[-2:]
    team = "_".join(team.split("-")[:-1])
    path = "player_data" + os.sep + year + os.sep + team
    if not os.path.isdir(path):
        os.mkdir(path)
    return(path)


# Function that grabs all the players from one club page
def get_all_players(url, players):
    # initialize dictionary and web page
    d = wd.init_loaded_page_id(url, "stats_misc_9")
    t_id = "stats_standard_9"

    # Traverse page to find table with all players
    stat = d.find_element(By.ID, t_id)
    trs = stat.find_elements(By.CSS_SELECTOR, "tr")

    # Go through each row and grab player and link to them 
    for row in trs:
        e = row.find_elements(By.CSS_SELECTOR, "a")
        if len(e) != 0 and e[0].text not in players.keys():
            players[e[0].text] = get_player_tm(e[0].get_attribute("href"))
    d.close()
    return players


def get_player_tm(url):
    new_link = ""
    d = wd.init_loaded_page_id(url, "div_resources_other")
    try:
        ext_links = d.find_element(By.ID, "div_resources_other")
    except NoSuchElementException as e:
        d.close()
        return ""
    else:
        ext_links = d.find_element(By.ID, "div_resources_other")
        for link in ext_links.find_elements(By.CSS_SELECTOR, "a"):
            if link.text.find("markt") != -1:
                new_link = link.get_attribute("href").replace("profil", "marktwertverlauf")
                break

    d.close()
    return new_link
