import numpy as np
import pandas as pd
import itertools


df = pd.read_excel('Eric Manual CV (1).xlsx', nrows=5)

for index, row in df.iterrows():
    combinations = [x for x in itertools.combinations(row[1:], 3)]
    bestStd = 999999999
    bestCombination = None
    for i in range(len(combinations)):
        std = np.std(combinations[i])
        if std < bestStd:
            bestStd = std
            bestCombination = combinations[i]
    bestMean = np.mean(bestCombination)
    print('CV:', (bestStd/bestMean*100), "std:", bestStd, "mean", bestMean, "combination", bestCombination)
print(.0683094506583124*12.18)
print('Were so Fucked')


