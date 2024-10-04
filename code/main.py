from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

stand_site = "https://fbref.com/en/comps/9/2023-2024/stats/2023-2024-Premier-League-Stats"
stand_id = "stats_standard"
standard_stats = ["player",
"nationality",
"position",
"team",
"age",
"games",
"games_starts",
"minutes",
"minutes_90s",
"goals",
"assists",
"pens_made",
"pens_att",
"cards_yellow",
"cards_red",
"xg",
"npxg",
"xg_assist",
"progressive_carries",
"progressive_passes",
"progressive_passes_received"]


goal_site = "https://fbref.com/en/comps/9/2023-2024/keepers/2023-2024-Premier-League-Stats"
goal_id = "stats_keeper"
goal_stats = ["gk_goals_against",
"gk_shots_on_target_against",
"gk_saves",
"gk_wins",
"gk_ties",
"gk_losses",
"gk_clean_sheets",
"gk_pens_att",
"gk_pens_allowed",
"gk_pens_saved",
"gk_pens_missed"]



adgoal_site = "https://fbref.com/en/comps/9/2023-2024/keepersadv/2023-2024-Premier-League-Stats"
adgoal_id = "stats_keeper_adv"
adgoal_stats = ["gk_free_kick_goals_against",
"gk_corner_kick_goals_against",
"gk_psxg",
"gk_psnpxg_per_shot_on_target_against",
"gk_psxg_net",
"gk_passes_completed_launched",
"gk_passes_launched",
"gk_passes",
"gk_passes_throws",
"gk_passes_length_avg",
"gk_goal_kicks",
"gk_goal_kick_length_avg",
"gk_crosses",
"gk_crosses_stopped",
"gk_def_actions_outside_pen_area",
"gk_avg_distance_def_actions"]


shot_site = "https://fbref.com/en/comps/9/2023-2024/shooting/2023-2024-Premier-League-Stats"
shot_id = "stats_shooting"
shot_stats = ["shots",
"shots_on_target",
"average_shot_distance",
"xg_net"]


pass_site = "https://fbref.com/en/comps/9/2023-2024/passing/2023-2024-Premier-League-Stats"
pass_id = "stats_passing"
pass_stats = ["passes_completed",
"passes",
"passes_total_distance",
"passes_progressive_distance",
"passes_completed_short",
"passes_short",
"passes_completed_medium",
"passes_medium",
"passes_completed_long",
"passes_long",
"pass_xa",
"assisted_shots",
"passes_into_final_third",
"passes_into_penalty_area",
"crosses_into_penalty_area"]


pt_site = "https://fbref.com/en/comps/9/2023-2024/passing_types/2023-2024-Premier-League-Stats"
pt_id = "stats_passing_types"
pt_stats = ["passes_live",
"passes_dead",
"passes_free_kicks",
"through_balls",
"passes_switches",
"crosses",
"throw_ins",
"corner_kicks",
"corner_kicks_in",
"corner_kicks_out",
"corner_kicks_straight",
"passes_completed",
"passes_offsides",
"passes_blocked"]


gca_site = "https://fbref.com/en/comps/9/2023-2024/gca/2023-2024-Premier-League-Stats"
gca_id = "stats_gca"
gca_stats = ["sca",
"sca_passes_live",
"sca_passes_dead",
"sca_take_ons",
"sca_shots",
"sca_fouled",
"sca_defense",
"gca",
"gca_passes_live",
"gca_passes_dead",
"gca_take_ons",
"gca_shots",
"gca_fouled",
"gca_defense"]


def_site = "https://fbref.com/en/comps/9/2023-2024/defense/2023-2024-Premier-League-Stats"
def_id = "stats_defense"
def_stats = ["tackles",
"tackles_won",
"tackles_def_3rd",
"tackles_mid_3rd",
"tackles_att_3rd",
"challenge_tackles",
"challenges",
"challenges_lost",
"blocked_shots",
"blocked_passes",
"interceptions",
"clearances",
"errors"]


poss_site = "https://fbref.com/en/comps/9/2023-2024/possession/2023-2024-Premier-League-Stats"
poss_id = "stats_possession"
poss_stats = ["touches_def_pen_area",
"touches_def_3rd",
"touches_mid_3rd",
"touches_att_3rd",
"touches_att_pen_area",
"touches_live_ball",
"take_ons",
"take_ons_won",
"take_ons_tackled",
"carries",
"carries_distance",
"carries_progressive_distance",
"carries_into_final_third",
"carries_into_penalty_area",
"miscontrols",
"dispossessed",
"passes_received"]


time_site = "https://fbref.com/en/comps/9/2023-2024/playingtime/2023-2024-Premier-League-Stats"
time_id = "stats_playing_time"
time_stats = ["games_complete",
"games_subs",
"unused_subs",
"points_per_game",
"on_goals_for",
"on_goals_against",
"plus_minus_wowy",
"on_xg_for",
"on_xg_against"]


misc_site = "https://fbref.com/en/comps/9/2023-2024/misc/2023-2024-Premier-League-Stats"
misc_id = "stats_misc"
misc_stats = ["cards_yellow_red",
"fouls",
"fouled",
"offsides",
"pens_won",
"pens_conceded",
"own_goals",
"ball_recoveries",
"aerials_won",
"aerials_lost"]


years = ["2017-2018","2018-2019","2019-2020","2020-2021","2021-2022","2022-2023","2023-2024"]
tableNames = ["stats","shooting","gca","passing","passing_types","possession", "defense","playingtime","misc","keepers","keepersadv"]


driver = webdriver.Firefox()
driver.get(misc_site)




# rk = driver.find_element(By.CLASS_NAME,'ranker')
table = driver.find_element(By.ID, misc_id)
bod = table.find_element(By.CSS_SELECTOR, "tbody")
trs = bod.find_elements(By.CSS_SELECTOR, "tr")


for row in trs:
    if row.get_attribute("class") == 'thead':
        continue
    data = row.find_elements(By.CSS_SELECTOR, "td")
    print('row')
    for d in data:
        print(d.get_attribute("data-stat"))
    # for thing in row:
    #     print(thing.text)

    

    # print(row.text)



print(len(trs))
driver.close()