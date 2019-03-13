import numpy

import pandas as pd

#age, married, signal, divorced, primary, secondary, tertiary, default(0-1),balance,housing(0-1),loan(0-1), celluar, telephone, duration, campaign, pdays, previous
#failure, other, success, y

dataset = pd.read_csv("csv/bank.csv", sep=',').to_numpy()

X = dataset

a = numpy.empty((4521, 21), dtype=object)

b = []

for i in range(len(X)):
    a[i][0] = X[i][0]
    if X[i][1] == "married":
        a[i][1] = 1
        a[i][2] = 0
        a[i][3] = 0
    elif X[i][1] == "signal":
        a[i][1] = 0
        a[i][2] = 1
        a[i][3] = 0
    elif X[i][1] == "divorced":
        a[i][1] = 0
        a[i][2] = 0
        a[i][3] = 1
    else:
        a[i][1] = 0
        a[i][2] = 0
        a[i][3] = 0
    if X[i][2] == "primary":
        a[i][4] = 1
        a[i][5] = 0
        a[i][6] = 0
    elif X[i][2] == "secondary":
        a[i][4] = 0
        a[i][5] = 1
        a[i][6] = 0
    elif X[i][2] == "tertiaty":
        a[i][4] = 0
        a[i][5] = 0
        a[i][6] = 1
    else:
        a[i][4] = 0
        a[i][5] = 0
        a[i][6] = 0
    if X[i][3] == "no":
        a[i][7] = 0
    if X[i][3] == "yes":
        a[i][7] = 1
    a[i][8] = X[i][4]
    if X[i][5] == "no":
        a[i][9] = 0
    if X[i][5] == "yes":
        a[i][9] = 1
    if X[i][6] == "no":
        a[i][10] = 0
    if X[i][6] == "yes":
        a[i][10] = 1
    if X[i][7] == "cellular":
        a[i][11] = 1
        a[i][12] = 0
    elif X[i][7] == "telephone":
        a[i][11] = 0
        a[i][12] = 1
    else:
        a[i][11] = 0
        a[i][12] = 0
    a[i][13] = X[i][8]
    a[i][14] = X[i][9]
    a[i][15] = X[i][10]
    a[i][16] = X[i][11]
    if (X[i][12]) == "failure":
        a[i][17] = 1
        a[i][18] = 0
        a[i][19] = 0
    elif (X[i][12]) == "other":
        a[i][17] = 0
        a[i][18] = 1
        a[i][19] = 0
    elif (X[i][12]) == "success":
        a[i][17] = 0
        a[i][18] = 0
        a[i][19] = 1
    else:
        a[i][17] = 0
        a[i][18] = 0
        a[i][19] = 0
    if X[i][13] == "no":
        a[i][20] = 0
    if X[i][13] == "yes":
        a[i][20] = 1

numpy.savetxt("csv/boolean_bank.csv", a, delimiter=',', fmt='% 4d')