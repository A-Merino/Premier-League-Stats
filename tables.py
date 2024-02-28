import csv
import pandas as pd
import numpy as np


def table_cleaner(table):
    ex = ["Playing","Standard" , "Goals", "Total", "Pass", "SCA", "Tackles", "Touches", "Performance"]
    with open("tab.csv", "w") as file:
        writ = csv.writer(file, delimiter=",")

        for i, line in enumerate(table.split("\n")):

            line = line.split(" ")
            line.remove(line[-1])

            if line[0] in ex:
                continue
            elif line[0] != "Player":
                line[0] = " ".join((line[0], line[1]))
                line.remove(line[2])
                line.remove(line[1])
            elif i != 1:
                continue
            # print(line)
            line.remove(line[1])
            while "Pen" in line:
                line.remove("Pen")
            while "3rd" in line:
                line.remove("3rd")
            while "(GK)" in line:
                line.remove("(GK)")
            writ.writerow(line)


def table_joiner(df):
    table = pd.read_csv("tab.csv", encoding="latin1")
    table = table.iloc[:-2,:]
    if df.empty:
        return table
    return pd.concat([table, df])
    # return pd.merge(table, df, how="left")

