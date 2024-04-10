import pandas as pd, numpy as np, matplotlib, matplotlib.pyplot as plt


nbLineShowed = 10
def showDF(df, nbLine=nbLineShowed):
    if nbLine <= 0 :
        print(df,'\n')
    else :
        print(df.head(nbLine),'\n')

dataClient = pd.read_csv('base_comptoir_espace_table_clients.csv', sep=';')
dataEntreprise = pd.read_csv('base_comptoir_espace_table_decisions_entreprises.csv', sep=';')



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

def q1g1():
    """
    Produire les graphiques joints à partir de données extraites de ces deux tables
    et donner pour chacun de ces graphiques une interprétation de la représentation en
    choisissant un cas particulier, exemple "part de marché sur l'année 1 en quantité des
    différente entreprise sur le produit 1"
    """
    print("Question 1 : Part de marché sur l'année 1 en quantité des différente entreprise sur le produit 1\n")
    # Pandas stuff
    cliMask1 = (dataClient.CLI_PROD == 1)&(dataClient.CLI_CHOIX != 0)&(dataClient.CLI_ANNEE == 1)
    cliMask2 = (dataClient.CLI_PROD == 1)&(dataClient.CLI_CHOIX != 0)&(dataClient.CLI_ANNEE == 2)
    cliP1A1 = dataClient[cliMask1][['CLI_ID', 'CLI_CHOIX']]
    cliP1A2 = dataClient[cliMask2][['CLI_ID', 'CLI_CHOIX']]
    showDF(cliP1A1)
    showDF(cliP1A2)
    
    # Pyplot Stuff
    fig1, axs1 = plt.subplots(ncols=2)
    fig1.suptitle("Part de marché sur l'année en quantité des différente entreprise sur le produit 1")
    stat1 = cliP1A1.groupby(['CLI_CHOIX']).count()
    stat2 = cliP1A2.groupby(['CLI_CHOIX']).count()
    axs1[0].pie(stat1['CLI_ID'], labels=[f"entreprise n°{i+1}" for i in range(cliP1A1['CLI_CHOIX'].nunique())], autopct='%.0f%%')
    axs1[1].pie(stat2['CLI_ID'], labels=[f"entreprise n°{i+1}" for i in range(cliP1A1['CLI_CHOIX'].nunique())], autopct='%.0f%%')
    
    plt.legend()
    plt.show()

def q1g2():
    # Pandas Stuff
    maskA1 = (dataEntreprise.ENT_ANNEE==1)
    maskA2 = (dataEntreprise.ENT_ANNEE==2)
    dataA1 = dataEntreprise[maskA1][['ENT_ID', 'ENT_PRIX']]
    dataA2 = dataEntreprise[maskA2][['ENT_ID', 'ENT_PRIX']]
    showDF(dataA1)
    showDF(dataA2)
    
    statA1 = dataA1.groupby(['ENT_ID']).sum('ENT_PRIX')
    statA2 = dataA2.groupby(['ENT_ID']).sum('ENT_PRIX')
    
    # Pyplot Stuff
    fig2, axs2 = plt.subplots()
    barWidth = 0.5
    fig2.suptitle("Chiffre d'affaire des entreprise sur les 2 première année")
    axs2.bar(label="Année 1", width=barWidth/2, align="edge", height=statA1['ENT_PRIX'], x=[f"entreprise n°{i+1}" for i in range(dataA1['ENT_ID'].nunique())])
    axs2.bar(label="Année 2", width=-barWidth/2, align="edge", height=statA2['ENT_PRIX'], x=[f"entreprise n°{i+1}" for i in range(dataA2['ENT_ID'].nunique())])
    
    plt.legend()
    plt.show()

def q1g3():
    # Pandas Stuff
    cliMask = (dataClient.CLI_PROD == 1)&(dataClient.CLI_ANNEE == 1)
    e1Mask = (dataClient.CLI_CHOIX == 1)
    e2Mask = (dataClient.CLI_CHOIX == 2)
    e3Mask = (dataClient.CLI_CHOIX == 3)
    e4Mask = (dataClient.CLI_CHOIX == 4)
    dataCliE1 = dataClient[cliMask&e1Mask][['CLI_ID', 'CLI_PRIX']]
    dataCliE2 = dataClient[cliMask&e2Mask][['CLI_ID', 'CLI_PRIX']]
    dataCliE3 = dataClient[cliMask&e3Mask][['CLI_ID', 'CLI_PRIX']]
    dataCliE4 = dataClient[cliMask&e4Mask][['CLI_ID', 'CLI_PRIX']]
    showDF(dataCliE1, 0)
    
    # Pyplot Stuff

def main():
    showInfo = False
    if showInfo :
        showDF(dataClient, 0)
        showDF(dataEntreprise, 0)
    
    q1g1()
    q1g2()
    q1g3()
    
if __name__=="__main__":{
    main()
}