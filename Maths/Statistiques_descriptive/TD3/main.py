import pandas as pd, numpy as np, matplotlib, matplotlib.pyplot as plt
from scipy.stats import linregress


nbLineShowed = 10
def showDF(df, nbLine=nbLineShowed):
    if nbLine <= 0 :
        print(df,'\n')
    else :
        print(df.head(nbLine),"\n\n")


dPlayer = pd.read_csv('data_players.csv', sep=',')
dScores = pd.read_csv('match_scores.csv', sep=';')
dStats = pd.read_csv('match_stats.csv', sep=';')
dTournaments = pd.read_csv('tournaments.csv', sep=';')
dRanking1 = pd.read_csv('rankings.csv', sep=';')
dRanking2 = pd.read_csv('rankings_2.csv', sep=';')
dRanking3 = pd.read_csv('rankings_3.csv', sep=';')


def g1():
    grandJoueurs = dPlayer[(dPlayer.height_cm > 6.5) & (dPlayer.birth_year > 1960.0)]['height_cm']
    print(grandJoueurs.describe())
    
    bmin = grandJoueurs.min()
    bmax = grandJoueurs.max()
    liBo = [i for i in range(int(bmin), int(bmax), 5)]
    print(liBo)
    plt.hist(x=grandJoueurs, bins=liBo,ec='black')
    plt.title("Distribution des tailles des joueur nées à partir de 1960")
    plt.show()

if __name__ == "__main__":
    debug = False
    if debug :
        print("Player\n")
        showDF(dPlayer)
        print("Scores\n")
        showDF(dScores)
        print("Stats\n")
        showDF(dStats)
        print("Tournament\n")
        showDF(dTournaments)
        print("Ranking\n")
        showDF(dRanking1)
        showDF(dRanking2)
        showDF(dRanking3)

    # print(dPlayer.columns)
    g1()