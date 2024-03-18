import csv
import pandas as pd
import numpy as np


def table_cleaner(table):
    # excludes the top rows of the tables
    ex = ["Playing","Standard" , "Goals", "Total", "Pass", "SCA", "Tackles", "Touches", "Performance"]
    
    # open a new csv file with a writer
    with open("tab.csv", "w") as file:
        writ = csv.writer(file, delimiter=",")

        for i, line in enumerate(table.split("\n")):
            # Split the text data by cell (space character)
            line = line.split(" ")
            # Remove "Matches" column
            line.remove(line[-1])

            # Dont write the row with useless header
            if line[0] in ex:
                continue
            elif line[0] != "Player":
                # Put first and last name together into one cell 
                line[0] = " ".join((line[0], line[1]))
                line.remove(line[2])
                line.remove(line[1])
            elif i != 1:
                continue
            # print(line)
            line.remove(line[1])
            # Some columns have spaces in name, so getting rid of extra columns
            while "Pen" in line:
                line.remove("Pen")
            while "3rd" in line:
                line.remove("3rd")
            while "(GK)" in line:
                line.remove("(GK)")

            # Write the line
            writ.writerow(line)


def table_joiner(df):
    table = pd.read_csv("tab.csv")
    table = table.iloc[:-2,:]
    if df.empty:
        return table
    return pd.concat([table, df])
    # return pd.merge(table, df, how="left")

