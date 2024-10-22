from data_class import SiteStats
import web_stuff as wb
import csv
import os
import numpy as np
import pandas as pd

def collectAllData():

    # import web table data
    st = SiteStats()
    

    for year in st.years: # Go through year list
        # Initialize variables 
        players = {}
        count = 1
        
        # t = table
        for t in st.tableNames.keys(): # Go through the different tables for each year

            # When code breaks (it has multiple times):
            # Grab names from standard table
            if os.path.isfile(f"../data/{year}/{year}stats_standard.csv") and st.tableNames[t][0] == "stats_standard":

                with open (f"../data/{year}/{year}{st.tableNames[t][0]}.csv", 'r', newline='') as file:
                    # Open csv and create a reader
                    read = csv.reader(file, delimiter=",")
                    # Insert player names into dictionary
                    for row in read:
                        players[row[2]] = []
                continue

            # Skip all other tables that exist
            elif os.path.isfile(f"../data/{year}/{year}{st.tableNames[t][0]}.csv"):
                continue
            
            # format website link
            site = "/".join(("https://fbref.com/en/comps/9",year, t,year+"-Premier-League-Stats"))
            # Run the site and grab players from the table
            data = wb.runSite(site, st.tableNames[t][0],st.tableNames[t][1])

            # Open a new file 
            with open(f"../data/{year}/{year}{st.tableNames[t][0]}.csv", "w", newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=",")
                # For each player in data collected
                for p in data:
                    # if not in dictionary, give id and add to dictionary
                    if t == "stats":
                        y = year.split("-")[1]
                        p.insert(1, int(f"1{y}{count:04d}"))
                        players[p[2]] = p
                        count += 1
                        writer.writerow(p)
                    # Add to list in dictionary if alredy there
                    elif p[1] in players.keys():
                        players[p[1]].extend(p[1:])

                        # Write to csv to save
                        writer.writerow(p[1:])



def csvCompiler():
    # data pulled for iterating
    st = SiteStats()

    for year in st.years:
        # Create dictionary of players
        players = {}

        # t = table
        for t in st.tableNames.keys():
            # Open all csvs in a year and get the players for them
            with open(f"../data/{year}/{year}{st.tableNames[t][0]}.csv", "r") as temp:
                tr = csv.reader(temp, delimiter=",")
                for row in tr:
                    # Add all data from standard csv
                    if t == "stats":
                        players[row[2]] = row
                    # Add data to other csvs based on name
                    else:
                        players[row[0]].extend(row[1:])

        # Create new csv for full data and write players to csv
        with open(f"../data/{year}/{year}full.csv", "w+", newline="") as full:
            writer = csv.writer(full, delimiter=",")
            for p in players.values():
                if len(p) != 146:
                    # If not a goalie, append zeros
                    p.extend(np.zeros(147-len(p)))
                    writer.writerow(p)
                else:
                    writer.writerow(p)


def addHeaders():
    st = SiteStats()

    for year in st.years:
        df = pd.read_csv(f'..\\data\\{year}\\{year}full.csv', header=None)
        df.to_csv(f'..\\data\\{year}\\{year}full2.csv', header=st.header, index=False)



# collectAllData()
# csvCompiler()
# addHeaders()



def rans():
    print(np.random.random([3,3])*4 - 2)

rans()