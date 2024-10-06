import csv
players = {}
year = "2017-2018"
g = "stats_standard"
with open (f"../data/{year}/{year}{g}.csv", 'r', newline='') as file:
    read = csv.reader(file, delimiter=",")
    for row in read:
        players[row[2]] = row

print(players)