import csv
import pandas as pd
import numpy as np


def table_cleaner(table):
    with open("tab.csv", "w") as file:
        writ = csv.writer(file, delimiter=",")

        for i, line in enumerate(table.split("\n")):

            line = line.split(" ")
            line.remove(line[-1])

            if line[0] == "Playing":
                continue
            elif line[0] != "Player":
                line[0] = " ".join((line[0], line[1]))
                line.remove(line[2])
                line.remove(line[1])
            elif i != 1:
                continue

            line.remove(line[1])
            writ.writerow(line)


def table_joiner(df):
    table = pd.read_csv("tab.csv")
    print(table)
