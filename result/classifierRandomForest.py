# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 22:33:43 2020

@author: xdcao@zju.edu.cn
"""

import collections
import random
from sklearn.ensemble import RandomForestClassifier

file = "data.txt"
f = open(file)

data = []
for ti in range(1, 45):
    data.append(f.readline().split())
f.close()
result = collections.defaultdict(int)
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

    model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=2)
    model.fit(X_train, Y_train)
    prediction = model.predict(X_test)
    result[(Y_test[0], prediction[0])] += 1