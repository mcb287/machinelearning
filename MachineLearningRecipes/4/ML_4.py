Python 3.5.3 (v3.5.3:1880cb95a742, Jan 16 2017, 16:02:32) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from sklearn import datasets
>>> iris = datasets.load_iris
>>> iris = datasets.load_iris()
>>> X = iris.data
>>> y = iris.target
>>> 
>>> from sklearn.cross_validation import train_test_split

Warning (from warnings module):
  File "E:\Program Files\WinPython-64bit-3.5.3.1Qt5\python-3.5.3.amd64\lib\site-packages\sklearn\cross_validation.py", line 44
    "This module will be removed in 0.20.", DeprecationWarning)
DeprecationWarning: This module was deprecated in version 0.18 in favor of the model_selection module into which all the refactored classes and functions are moved. Also note that the interface of the new CV iterators are different from that of this module. This module will be removed in 0.20.
>>> X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .5)
>>> from sklearn import tree
>>> my_classifier = tree.DecisionTreeClassifier()
>>> my_classifier.fit(X_train, y_train)
DecisionTreeClassifier(class_weight=None, criterion='gini', max_depth=None,
            max_features=None, max_leaf_nodes=None,
            min_impurity_split=1e-07, min_samples_leaf=1,
            min_samples_split=2, min_weight_fraction_leaf=0.0,
            presort=False, random_state=None, splitter='best')
>>> predictions = my_classifier.predict(X_test)
>>> print(predictions)
[2 2 2 2 1 2 2 0 2 0 2 2 2 1 0 1 1 1 0 0 1 0 1 0 0 1 0 1 1 1 1 2 2 1 2 2 2
 0 1 1 1 1 0 0 1 1 0 1 2 2 2 2 2 1 2 2 2 1 2 1 0 1 0 2 0 0 0 1 1 0 1 2 2 0
 1]
>>> from sklearn.metrics import accuracy_score
>>> print(accuracy_score(y_test, predictions))
0.96
>>> from sklearn.neighbors import KNeighborsClassifier
>>> my_classifier = KNeighborsClassifier()
>>> my_classifier.fit(X_train, y_train)
KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',
           metric_params=None, n_jobs=1, n_neighbors=5, p=2,
           weights='uniform')
>>> predictions = my_classifier.predict(X_test)
>>> print(accuracy_score(y_test, predictions))
0.92
>>> 
