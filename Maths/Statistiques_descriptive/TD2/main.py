import pandas as pd, numpy as np, matplotlib, matplotlib.pyplot as plt


nbLineShowed = 10
def showDF(df, nbLine=nbLineShowed):
    if nbLine <= 0 :
        print(df,'\n')
    else :
        print(df.head(nbLine),"\n\n")

dataClient = pd.read_csv('base_comptoir_espace_table_clients.csv', sep=';')
dataEntreprise = pd.read_csv('base_comptoir_espace_table_decisions_entreprises.csv', sep=';')


def g1():
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

def g2():
    # Pandas Stuff
    prixParClient = pd.merge(left=dataEntreprise, right=dataClient, how='inner', left_on=['ENT_ID', 'ENT_PROD', 'ENT_ANNEE'], right_on=['CLI_CHOIX', 'CLI_PROD', 'CLI_ANNEE'])
    
    maskA1 = (prixParClient.ENT_ANNEE==1)
    maskA2 = (prixParClient.ENT_ANNEE==2)
    dataA1 = prixParClient[maskA1][['ENT_ID', 'ENT_PRIX']]
    dataA2 = prixParClient[maskA2][['ENT_ID', 'ENT_PRIX']]
    showDF(dataA1)
    showDF(dataA2)
    
    statA1 = dataA1.groupby(['ENT_ID'])[['ENT_PRIX']].sum()
    statA2 = dataA2.groupby(['ENT_ID'])[['ENT_PRIX']].sum()
    # print(statA1, "\n\n", statA2)
    
    
    # Pyplot Stuff
    fig2, axs2 = plt.subplots()
    barWidth = 0.5
    fig2.suptitle("Chiffre d'affaire des entreprise sur les 2 première année")
    axs2.bar(label="Année 1", width=-barWidth/2, align="edge", height=statA1['ENT_PRIX'], x=[f"entreprise n°{i+1}" for i in range(dataA1['ENT_ID'].nunique())])
    axs2.bar(label="Année 2", width=barWidth/2, align="edge", height=statA2['ENT_PRIX'], x=[f"entreprise n°{i+1}" for i in range(dataA2['ENT_ID'].nunique())])
    
    plt.legend()
    plt.show()

def g3():
    # Pandas Stuff
    cliMask = (dataClient.CLI_PROD == 1)&(dataClient.CLI_ANNEE == 1)
    e1Mask = (dataClient.CLI_CHOIX == 1)
    e2Mask = (dataClient.CLI_CHOIX == 2)
    e3Mask = (dataClient.CLI_CHOIX == 3)
    e4Mask = (dataClient.CLI_CHOIX == 4)
    dataCliE1 = dataClient[cliMask&e1Mask][['CLI_PRIX']]
    dataCliE2 = dataClient[cliMask&e2Mask][['CLI_PRIX']]
    dataCliE3 = dataClient[cliMask&e3Mask][['CLI_PRIX']]
    dataCliE4 = dataClient[cliMask&e4Mask][['CLI_PRIX']]
    showDF(dataCliE1, 0)
    
    # Pyplot Stuff
    fig, axs = plt.subplots(ncols=2, nrows=2, figsize=(8,20), sharey=True)
    fig.suptitle("Distribution des prix max attendus pour les client des différentes entreprises pour le produit 1 sur l'année 1")
    listBornes = [i*1000+2000 for i in range(16)]
    
    axs[0][0].hist(x=dataCliE1,bins=listBornes, label="Entreprise 1", color="green")
    axs[0][1].hist(x=dataCliE2,bins=listBornes, label="Entreprise 2", color="green")
    axs[1][0].hist(x=dataCliE3,bins=listBornes, label="Entreprise 3", color="green")
    axs[1][1].hist(x=dataCliE4,bins=listBornes, label="Entreprise 4", color="green")
    plt.legend()
    
    plt.show()

def main():
    showInfo = False
    if showInfo :
        showDF(dataClient, 0)
        showDF(dataEntreprise, 0)
    
    # g1()
    # g2()
    g3()
    
if __name__=="__main__":{
    main()
}