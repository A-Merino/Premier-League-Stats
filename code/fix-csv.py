from glob import glob
import pandas as pd


def dropRows():
    files = glob('player_data\\allteams\\hh\\*')

    for f in files:
        df = pd.read_csv(f)
        cols = [df.columns[-2],df.columns[-4],df.columns[-8],df.columns[-11],df.columns[-14],df.columns[-17],df.columns[-21],df.columns[-24],df.columns[-25],df.columns[-26],df.columns[-27],df.columns[-28],df.columns[-29],df.columns[-30],df.columns[-35],df.columns[-40],df.columns[-43],
                df.columns[-45],df.columns[-46],df.columns[-47],df.columns[-48],df.columns[-49],df.columns[-50],df.columns[-51],df.columns[-54],df.columns[-55],df.columns[-60],df.columns[-66],df.columns[-67],df.columns[-68],df.columns[-69],df.columns[-70],df.columns[-71],
                df.columns[-78],df.columns[-86],df.columns[-88],df.columns[-89],df.columns[-90],df.columns[-91],df.columns[-92],df.columns[-101],df.columns[-106],df.columns[-107],df.columns[-108],df.columns[-109],df.columns[-110],df.columns[-111],
                df.columns[-112],df.columns[-117],df.columns[-119],df.columns[-120],df.columns[-121],df.columns[-124],df.columns[-127],df.columns[-132],df.columns[-135],df.columns[-136],df.columns[-137],df.columns[-138],df.columns[-139],
                df.columns[-145],df.columns[-149],df.columns[-151],df.columns[-160],df.columns[-161],df.columns[-162],df.columns[-163],df.columns[-164],df.columns[-165],df.columns[-167],df.columns[-168],df.columns[-169],df.columns[-170],df.columns[-171],
                df.columns[-174],df.columns[-175],df.columns[-176],df.columns[-177],df.columns[-178],df.columns[-181],df.columns[-182],df.columns[-183],df.columns[-184],df.columns[-185],df.columns[-186],df.columns[-187],df.columns[-188],df.columns[-189],
                df.columns[-190],df.columns[-191],df.columns[-192],df.columns[-193],df.columns[-194],df.columns[-195],df.columns[-199],df.columns[-211],df.columns[-212],df.columns[-213],df.columns[-214],df.columns[-215],df.columns[-216],df.columns[-217],
                df.columns[-218],df.columns[-219],df.columns[-220],df.columns[-224],df.columns[-225],df.columns[-230],df.columns[-233],df.columns[-235],df.columns[-236],df.columns[-237],df.columns[-240],df.columns[-241],df.columns[-242],
                ]
        df = df.drop(cols, axis=1)

        nf = f.replace('\\hh', '')
        df.to_csv(nf)


files = glob('player_data\\allteams\\*')
for f in files:
    if 'csv' in f:
        df = pd.read_csv(f)
        start = df.shape[0]
        df = df.dropna()
        end = df.shape[0]
        if start != end:
            print(f)




