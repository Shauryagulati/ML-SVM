# -*- coding: utf-8 -*-
"""SVM

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vsu-lgi-Ts313xTNoKc6vUYcfAAR81rm
"""

import sklearn
from sklearn import svm
from sklearn import datasets

cancer = datasets.load_breast_cancer()

print("Features: ", cancer.feature_names)

print("Labels: ", cancer.target_names)

x = cancer.data  # All of the features
y = cancer.target  # All of the labels

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.2)

print(x_train[:5], y_train[:5])

print(x_train, y_train)

from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier

clf = svm.SVC(kernel="linear")

clf.fit(x_train, y_train)

y_pred = clf.predict(x_test)

acc = metrics.accuracy_score(y_test, y_pred)

print(acc)

