from players import Player

years = ["2017-2018","2018-2019","2019-2020","2020-2021","2021-2022","2022-2023","2023-2024"]
tableNames = ["stats","shooting","gca","passing","passing_types","possession", "defense","playingtime","misc","keepers","keepersadv"]

misc_site = "https://fbref.com/en/comps/9/2023-2024/misc/2023-2024-Premier-League-Stats"

players = []
count = 1
playerObjs = []


for year in years:
    for t in tableNames:
        site = "/".join(("https://fbref.com/en/comps/9",year, t,year+"-Premier-League-Stats"))
        print(site)

if p not in players:
    playerObjs.append(Player(p, int(f"{year.split("-")[1]}{count:04d}")))
    count += 1
    