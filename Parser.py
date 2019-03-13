import numpy

import pandas as pd

dataset = pd.read_csv("bank.csv", sep=',').to_numpy()

X = dataset

for i in range(len(X)):
    for j in range (0, 14):
        if X[i][j] == "no":
            X[i][j] = 0
        elif X[i][j] == "yes":
            X[i][j] = 1
        elif X[i][j] == "married":
            X[i][j] = 0
        elif X[i][j] == "single":
            X[i][j] = 1
        elif X[i][j] == "divorced":
            X[i][j] = 2
        elif X[i][j] == "primary":
            X[i][j] = 0
        elif X[i][j] == "secondary":
            X[i][j] = 1
        elif X[i][j] == "tertiary":
            X[i][j] = 2
        elif X[i][j] == "cellular":
            X[i][j] = 1
        elif X[i][j] == "unknown":
            X[i][j] = 0
        elif X[i][j] == "telephone":
            X[i][j] = 2
        elif X[i][j] == "failure":
            X[i][j] = 1
        elif X[i][j] == "other":
            X[i][j] = 2
        elif X[i][j] == "success":
            X[i][j] = 3

numpy.savetxt("my_bank.csv", X, delimiter=',', fmt='% 4d')