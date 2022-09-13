import openskill
import csv
import os
from openskill import Rating, rate
from openskill.models import BradleyTerryFull
from tabulate import tabulate
import pandas as pd

#
#import csv
#
df = pd.read_csv(r'C:\Users\poiso\PycharmProjects\UT4OpenSkill\UTDuelClean2022.csv')
#print(df)
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

max = len(df)
print(max)

while index < 15542:
    winners = df[index:index+1]
    losers = df[index+1:index+2]

    print(winners)
    print(losers)

    index = index + 2

    winner0 = winners.values[0, 1]

    loser0 = losers.values[0, 1]

    print(loser0)

    ############

    winner0ELO = allplayers.loc[allplayers['name'] == winner0]
    winner0mu = winner0ELO.values[0, 1]
    winner0sig = winner0ELO.values[0, 2]
    w0 = Rating(winner0mu, winner0sig)
    print("initial elo")
    print(w0)
    print("####")

    ########
    loser0ELO = allplayers.loc[allplayers['name'] == loser0]
    loser0mu = loser0ELO.values[0, 1]
    loser0sig = loser0ELO.values[0, 2]
    l0 = Rating(loser0mu, loser0sig)
    print(l0)

    ########

    [[w0], [l0]] = rate([[w0], [l0]])

    print("Updated ELO")
    print(w0)
    print(l0)
    #############

    w0index = allplayers.loc[allplayers['name'] == winner0].index[0]
    print(w0index)
    print(type(allplayers))
    allplayers.at[w0index, 'mu'] = w0.mu
    allplayers.at[w0index, 'sigma'] = w0.sigma


    ###################

    l0index = allplayers.loc[allplayers['name'] == loser0].index[0]
    allplayers.at[l0index, 'mu'] = l0.mu
    allplayers.at[l0index, 'sigma'] = l0.sigma


allplayers.to_csv("C:\out\Duel_OUTdefault2022_2.csv", sep='\t', encoding='utf-8')
print(allplayers)
