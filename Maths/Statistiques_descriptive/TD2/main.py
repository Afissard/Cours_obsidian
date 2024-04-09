import pandas as pd, numpy as np, matplotlib, matplotlib.pyplot as plt


nbLineShowed = 10
def showDF(df, nbLine=nbLineShowed):
    if nbLine <= 0 :
        print(df,'\n')
    else :
        print(df.head(nbLine),'\n')

dataClient = pd.read_csv('base_comptoir_espace_table_clients.csv', sep=';')
dataEntreprise = pd.read_csv('base_comptoir_espace_table_decisions_entreprises.csv', sep=';')
showDF(dataClient, 0)
showDF(dataEntreprise, 0)



# teamMask = (data_equipes.League == 'French Ligue 1 (1)')
# teamsDataNeeded = data_equipes[teamMask][['ID', 'Name', 'League']]
# playerDataNeeded = data_joueurs[['Name', 'Age', 'Club_id', 'WageEUR']]
# print(playerDataNeeded.head(5), "\n", teamsDataNeeded.head(5), "\n\n")

# mergedTab = pd.merge(left=teamsDataNeeded, right=playerDataNeeded, left_on=['ID'],right_on=['Club_id'])[['Name_x', 'Name_y', 'Age', 'WageEUR']]
# mergedTab.rename(columns={'Name_x': 'Club_Name', 'Name_y': 'Player_Name'})
# print(mergedTab.head(5), "\n\n")

# stats_transport=reponses.groupby(['moyens_transport']).count()
# print(stats_transport)
# plt.pie(stats_transport['humeurs'],labels=stats_transport.index.values,autopct=lambda pct:'{:.1f}%\neff={:d}'.format(pct,int(pct/100*stats_transport['humeurs'].sum())))
# #ou plus simplement : autopct='%.1f%%' mais la maîtrise des formats n'est pas exigée
# plt.show()

def q1():
    """
    Produire les graphiques joints à partir de données extraites de ces deux tables
    et donner pour chacun de ces graphiques une interprétation de la représentation en
    choisissant un cas particulier, exemple "part de marché sur l'année 1 en quantité des
    différente entreprise sur le produit 1"
    """
    print("Question 1 : Part de marché sur l'année 1 en quantité des différente entreprise sur le produit 1\n")
    cliMask = (dataClient.CLI_PROD == 1)&(dataClient.CLI_CHOIX != 0)&(dataClient.CLI_ANNEE == 1) 
    cliP1 = dataClient[cliMask][['CLI_ID', 'CLI_CHOIX']]
    showDF(cliP1)
    stat = cliP1.groupby(['CLI_CHOIX']).count()
    plt.pie(stat['CLI_ID'], labels=[f"entreprise n°{i+1}" for i in range(cliP1['CLI_CHOIX'].nunique())], autopct='%.0f%%')
    plt.show()

def main():
    q1()
    
if __name__=="__main__":{
    main()
}