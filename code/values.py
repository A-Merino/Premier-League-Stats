import os
from data_class import SiteStats
import csv
from glob import glob
import re
import json
import pandas as pd

def getPlayers():

    st = SiteStats()
    # get all file paths needed
    files = glob("..\\data\\*\\*")
    years = glob("..\\data\\*")

    # Go through each year of data
    for year in years:

        links = {}
        # Create filepath for specific file in each path
        y = year + "\\" + year.split("\\")[-1] + "full.csv"
        
        with open(y, 'r') as file:
            read = csv.reader(file, delimiter=",")
            for row in read:
                # Check if the player is in the list, if not add it
                if row[0] not in links:
                    links[row[0].split("/")[-1].lower()] = row[2]
 
        # Create the path for the json file
        pj = "..\\..\\transfermarkt-datasets\\data\\raw\\transfermarkt-scraper\\" + year.split("-")[1] + "\\players.json"

        players = [["Name", "TMID"]]

        with open(pj, "r") as file:
            for f in file:
                # Get the link for the team of the player
                cur_link = f.split('"href": "/')[1][:-2].split('/')[0]
                if cur_link in links.keys(): 
                    # Get the link for the player which contains the id
                    pl = f.split('"href": ')[1].split(', "parent"')[0].strip('"')
                    # Get id from link
                    pid = pl.split("/")[-1]
                    #Regex is used to replace escape characters with question marks

                    # First name
                    fn = re.sub(r"\\.{5}", "?", f.split('", "last_name": "')[0].split('"')[-1])
                    # Last Name
                    ln = re.sub(r"\\.{5}", "?", f.split('"last_name": "')[1].split('"')[0])

                    players.append([links[cur_link], int(pid)])  # Add to list

        # Create a new csv
        with open(f"..\\data\\{year}\\playerTM.csv", "w", newline="") as file2:
            fw = csv.writer(file2, delimiter=",")
            # Save the data to a csv
            for p in players:
                fw.writerow(p)


def getPlayerValues():
    # Get data
    st = SiteStats()

    # For each year
    for year in st.years:
        # Get path of values
        pj2 = "..\\..\\transfermarkt-datasets\\data\\raw\\transfermarkt-api\\" + year.split("-")[1] + "\\market_values.json"

        # Get file for players
        pfile = f"..\\data\\{year}\\playerTM.csv"
        players = {}

        # Open players files
        with open(pfile, "r") as file:
            # Create a csv file reader
            read = csv.reader(file, delimiter=",")
            next(read)  # Skip header

            # For loop to get all player id's in a
            # Dictionary 
            for row in read:
                players[row[1]] = [row[0]]

        # print(players.keys())

        # Open market values file
        with open(pj2, "r") as file2:

            for row in file2:
                # Check for rows in file that are players from league in this season
                cur_id = row.split('"player_id": ')[1].replace("}", "").strip()
                if cur_id in players.keys():
                    # Get list of values from dictionary 
                    all_values = json.loads(row.replace("\n", ""))['response']['list']
                    for val in all_values:
                        # Go through each value and check if it is from the current year 
                        if (year.split("-")[1]) in val["datum_mw"]:
                            
                            if "Dec" in val["datum_mw"] or "Jan" in val["datum_mw"] or "Feb" in val["datum_mw"] or "Oct" in val["datum_mw"] or "Mar" in val["datum_mw"] or "Sep" in val["datum_mw"]:
                                continue

                            # Add to list
                            players[cur_id].append(val["datum_mw"])
                            players[cur_id].append(val["y"])


        # Open a new csv file
        with open(f'..\\data\\{year}\\{year}values.csv', "w", newline="") as file3: 
            right = csv.writer(file3, delimiter=",")
            # Go through each player and add to file if they have a value
            for p in players.values():
                if len(p) != 1:
                    right.writerow(p)


def appendValues():
    # Get data
    st = SiteStats()

    # For each year
    for year in st.years:

        # Get file for players
        pfile = f"..\\data\\{year}\\{year}values.csv"
        values = {}

        # Open players files
        with open(pfile, "r") as file:
            # Create a csv file reader
            read = csv.reader(file, delimiter=",")
            next(read)  # Skip header

            # For loop to get all player id's in a
            # Dictionary 
            for row in read:
                values[row[0]] = row[1]

        # print(players.keys())

        full = f"..\\data\\{year}\\{year}full.csv"
        players = [st.header]

        # Open market values file
        with open(full, "r") as file2:
            read = csv.reader(file2, delimiter=",")
            next(read)  # Skip header

            for row in read:
                if row[2] in values.keys():
                    row.append(values[row[2]])
                    players.append(row)
                else:
                    players.append(row)


        # Open a new csv file
        with open(f'..\\data\\{year}\\{year}comp.csv', "w", newline="") as file3: 
            right = csv.writer(file3, delimiter=",")
            # Go through each player and add to file if they have a value
            for p in players:
                right.writerow(p)



# getPlayers()
# getPlayerValues()
# appendValues()