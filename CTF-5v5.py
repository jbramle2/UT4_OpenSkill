import openskill
import csv
from openskill import Rating, rate
from openskill.models import BradleyTerryFull
from tabulate import tabulate
import pandas as pd

#
#import csv
#
df = pd.read_csv(r'C:\Users\poiso\PycharmProjects\UT4OpenSkill\UTPugsOnlyCTF.csv')
print(df)
######################
#
#make table of unique names with default mu and sigma
#
names = df.name.unique()
print(names)
allplayers = pd.DataFrame(data=names)
allplayers["mu"] = 25
allplayers["sigma"] = 8.333333333333334
allplayers.columns = ['name', 'mu', 'sigma']

pd.set_option("display.max_rows", None, "display.max_columns", None)
print(allplayers)

#######################
index = 0
index5 = index + 5
index10 = index5 + 5

max = len(df)

while index < max:
    winners = df[index:index5]
    losers = df[index5:index10]

    #print(winners)
    #print(losers)

    index = index10
    index5 = index + 5
    index10 = index5 + 5

    for x in range(0, 5):
        globals()[f"winner{x}"] = winners.values[x, 1]

    #print(winner0)

    for x in range(0, 5):
        globals()[f"loser{x}"] = losers.values[x, 1]

    #print(loser0)

    ############

    winner0ELO = allplayers.loc[allplayers['name'] == winner0]
    winner0mu = winner0ELO.values[0, 1]
    winner0sig = winner0ELO.values[0, 2]
    w0 = Rating(winner0mu, winner0sig)
    #print("initial elo")
    #print(w0)

    winner1ELO = allplayers.loc[allplayers['name'] == winner1]
    winner1mu = winner1ELO.values[0, 1]
    winner1sig = winner1ELO.values[0, 2]
    w1 = Rating(winner1mu, winner1sig)

    winner2ELO = allplayers.loc[allplayers['name'] == winner2]
    winner2mu = winner2ELO.values[0, 1]
    winner2sig = winner2ELO.values[0, 2]
    w2 = Rating(winner2mu, winner2sig)

    winner3ELO = allplayers.loc[allplayers['name'] == winner3]
    winner3mu = winner3ELO.values[0, 1]
    winner3sig = winner3ELO.values[0, 2]
    w3 = Rating(winner3mu, winner3sig)

    winner4ELO = allplayers.loc[allplayers['name'] == winner4]
    winner4mu = winner0ELO.values[0, 1]
    winner4sig = winner0ELO.values[0, 2]
    w4 = Rating(winner4mu, winner4sig)

    ########
    loser0ELO = allplayers.loc[allplayers['name'] == loser0]
    loser0mu = loser0ELO.values[0, 1]
    loser0sig = loser0ELO.values[0, 2]
    l0 = Rating(loser0mu, loser0sig)
    #print(l0)

    loser1ELO = allplayers.loc[allplayers['name'] == loser1]
    loser1mu = loser1ELO.values[0, 1]
    loser1sig = loser1ELO.values[0, 2]
    l1 = Rating(loser1mu, loser1sig)

    loser2ELO = allplayers.loc[allplayers['name'] == loser2]
    loser2mu = loser2ELO.values[0, 1]
    loser2sig = loser2ELO.values[0, 2]
    l2 = Rating(loser2mu, loser2sig)

    loser3ELO = allplayers.loc[allplayers['name'] == loser3]
    loser3mu = loser3ELO.values[0, 1]
    loser3sig = loser3ELO.values[0, 2]
    l3 = Rating(loser3mu, loser3sig)

    loser4ELO = allplayers.loc[allplayers['name'] == loser4]
    loser4mu = loser0ELO.values[0, 1]
    loser4sig = loser0ELO.values[0, 2]
    l4 = Rating(loser4mu, loser4sig)

    ########


    [[w0, w1, w2, w3, w4], [l0, l1, l2, l3, l4]] = rate([[w0, w1, w2, w3, w4], [l0, l1, l2, l3, l4]], model=BradleyTerryFull)

    #print("Updated ELO")
    #print(w0)
    #print(l0)
    #############

    w0index = allplayers.loc[allplayers['name'] == winner0].index[0]
    allplayers.at[w0index, 'mu'] = w0[0]
    allplayers.at[w0index, 'sigma'] = w0[1]

    w1index = allplayers.loc[allplayers['name'] == winner1].index[0]
    allplayers.at[w1index, 'mu'] = w1[0]
    allplayers.at[w1index, 'sigma'] = w1[1]

    w2index = allplayers.loc[allplayers['name'] == winner2].index[0]
    allplayers.at[w2index, 'mu'] = w2[0]
    allplayers.at[w2index, 'sigma'] = w2[1]

    w3index = allplayers.loc[allplayers['name'] == winner3].index[0]
    allplayers.at[w3index, 'mu'] = w3[0]
    allplayers.at[w3index, 'sigma'] = w3[1]

    w4index = allplayers.loc[allplayers['name'] == winner4].index[0]
    allplayers.at[w4index, 'mu'] = w4[0]
    allplayers.at[w4index, 'sigma'] = w4[1]

    ###################

    l0index = allplayers.loc[allplayers['name'] == loser0].index[0]
    allplayers.at[l0index, 'mu'] = l0[0]
    allplayers.at[l0index, 'sigma'] = l0[1]

    l1index = allplayers.loc[allplayers['name'] == loser1].index[0]
    allplayers.at[l1index, 'mu'] = l1[0]
    allplayers.at[l1index, 'sigma'] = l1[1]

    l2index = allplayers.loc[allplayers['name'] == loser2].index[0]
    allplayers.at[l2index, 'mu'] = l2[0]
    allplayers.at[l2index, 'sigma'] = l2[1]

    l3index = allplayers.loc[allplayers['name'] == loser3].index[0]
    allplayers.at[l3index, 'mu'] = l3[0]
    allplayers.at[l3index, 'sigma'] = l3[1]

    l4index = allplayers.loc[allplayers['name'] == loser4].index[0]
    allplayers.at[l4index, 'mu'] = l4[0]
    allplayers.at[l4index, 'sigma'] = l4[1]

allplayers.to_csv("UTPugsOnlyCTF_OUT.csv", sep='\t', encoding='utf-8')
print(allplayers)