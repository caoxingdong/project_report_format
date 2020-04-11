# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 22:11:52 2020

@author: xdcao@zju.edu.cn
"""

import collections
import random
from sklearn import svm

file = "data.txt"
f = open(file)

data = []
for ti in range(1, 45):
    data.append(f.readline().split())
f.close()
res = collections.defaultdict(int)
for j in range(1000): 
    X = []
    Y = []   
    random.shuffle(data)
    for i in range(44):
        X.append(data[i][1:4])
        Y.append(data[i][4])
    X_train = X[:-1]
    Y_train = Y[:-1]
    X_test = [X[-1]]
    Y_test = [Y[-1]]

    clf = svm.SVC(gamma='auto')
    clf.fit(X_train, Y_train)
    res[(Y_test[0], clf.predict(X_test)[0])] += 1