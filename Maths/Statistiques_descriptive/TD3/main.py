import pandas as pd, numpy as np, matplotlib, matplotlib.pyplot as plt
from scipy.stats import linregress


nbLineShowed = 10
def showDF(df, nbLine=nbLineShowed):
    if nbLine <= 0 :
        print(df,'\n')
    else :
        print(df.head(nbLine),"\n\n")


dPlayer = pd.read_csv('data_player.csv', sep=';')
dScores = pd.read_csv('match_scores.csv', sep=';')
dStats = pd.read_csv('match_stats.csv', sep=';')
dRanking = pd.read_csv('ranking.csv', sep=';')
dTournaments = pd.read_csv('tournament.csv', sep=';')