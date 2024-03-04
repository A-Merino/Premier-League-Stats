import web_driver as wd
import tables as tb
import pandas as pd
import numpy as np
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def get_team_sites(url, year):
    links = dict()
    # Each season requires a unique table id
    f, s = year.split('-')  
    ids = "".join(("results20", f, "-20", s, "91_overall"))

    # Create web driver and find season table
    d = wd.init_league_page(url, ids)
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
    players = dict()
    tables = ["stats_standard_9", "stats_shooting_9", "stats_passing_9",
            "stats_passing_types_9", "stats_gca_9", "stats_defense_9",
            "stats_possession_9", "stats_playing_time_9", "stats_misc_9",
            "stats_keeper_9", "stats_keeper_adv_9"]
    d = wd.init_club_page(url)
    club_stats = pd.DataFrame()
    for tab in tables:
        tb.table_cleaner(d.find_element(By.ID, tab).text)
        club_stats = tb.table_joiner(club_stats)
        # t.find_element(By.CLASS_NAME, " poptip sort_default_asc left").click()
        # print(tab)
    d.close()
    return club_stats

def get_all_players(url):
    players = dict()
    d = wd.init_club_page(url)
    t_id = "stats_standard_9"
    stat = d.find_element(By.ID, t_id)
    trs = stat.find_elements(By.CSS_SELECTOR, "tr")
    for row in trs:
        e = row.find_elements(By.CSS_SELECTOR, "a")
        # print(row.get_attribute("href"))
        # print(row.find_elements(By.CSS_SELECTOR, "a"))
        # for s in e:
        #     q = s.get_attribute("href")
        # print(e)
        if len(e) != 0:
            players[e[0].text] = e[0].get_attribute("href")
    d.close()
    return players

def player_tm(url):
    d = wd.init_tm_page(url)
