class SiteStats:

    def __init__(self):
        self.standard_stats = ["player",
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


        self.goal_stats = ["player","gk_goals_against",
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



        self.adgoal_stats = ["player","gk_free_kick_goals_against",
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


        self.shot_stats = ["player","shots",
        "shots_on_target",
        "average_shot_distance",
        "xg_net"]


        self.pass_stats = ["player","passes_completed",
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


        self.pt_stats = ["player","passes_live",
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


        self.gca_stats = ["player","sca",
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


        self.def_stats = ["player", "tackles",
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


        self.poss_stats = ["player","touches_def_pen_area",
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


        self.time_stats = ["player","games_complete",
        "games_subs",
        "unused_subs",
        "points_per_game",
        "on_goals_for",
        "on_goals_against",
        "plus_minus_wowy",
        "on_xg_for",
        "on_xg_against"]


        self.misc_stats = ["player","cards_yellow_red",
        "fouls",
        "fouled",
        "offsides",
        "pens_won",
        "pens_conceded",
        "own_goals",
        "ball_recoveries",
        "aerials_won",
        "aerials_lost"]


        self.years = ["2017-2018","2018-2019","2019-2020","2020-2021","2021-2022","2022-2023","2023-2024"]
        self.tableNames = {"stats":["stats_standard",self.standard_stats], "shooting":["stats_shooting", self.shot_stats], "gca":["stats_gca", self.gca_stats], 
                        "passing":["stats_passing", self.pass_stats], "passing_types":["stats_passing_types", self.pt_stats], "possession":["stats_possession", self.poss_stats],
                        "defense":["stats_defense", self.def_stats], "playingtime":["stats_playing_time", self.time_stats], "misc":["stats_misc", self.misc_stats], 
                        "keepers":["stats_keeper", self.goal_stats], "keepersadv":["stats_keeper_adv", self.adgoal_stats]}
