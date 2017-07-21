Python 3.5.3 (v3.5.3:1880cb95a742, Jan 16 2017, 16:02:32) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import sklearn
>>> 
 RESTART: G:\Git\Repositories\Machinelearning\MachineLearningRecipes\1\ML1.py 
>>> # Run Region [1-7]
>>> 
 RESTART: G:\Git\Repositories\Machinelearning\MachineLearningRecipes\1\ML1.py 
>>> from sklearn import tree
>>> features = [[140,1],[130,1],[150,0],[170,0]]
>>> labels = [0,0,1,1]
>>> clf = tree.DecisionTreeClassifier()
>>> clf = clf.fit(features, labels)
>>> clf.predict([[160,1]])
array([0])
>>> clf.predict([[160,1]])
array([0])
>>> clf.predict([[130,0]])
array([1])
>>> clf.predict([[130,1]])
array([0])
>>> clf.predict([[120,1]])
array([0])
>>> clf.predict([[100,1]])
array([0])
>>> clf.predict([[100,0]])
array([1])
>>> clf.predict([[190,0]])
array([1])
>>> features = [[140,1],[130,1],[150,0],[170,0],[180,1],[120,0]]
>>> labels = [0,0,1,1,1,0]
>>> clf = clf.fit(features, labels)
>>> clf.predict([[190,0]])
array([1])
>>> clf.predict([[190,1]])
array([1])
>>> clf.predict([[170,0]])
array([1])
>>> clf.predict([[130,0]])
array([0])
>>> clf.predict([[140,0]])
array([0])
>>> clf.predict([[150,0]])
array([1])
>>> clf.predict([[150,1]])
array([1])
>>> clf.predict([[140,1]])
array([0])
>>> clf.predict([[145,1]])
array([0])
>>> clf.predict([[145,0]])
array([0])
>>> clf.predict([[147,0]])
array([1])
>>> clf.predict([[147,1]])
array([1])
>>> clf.predict([[146,1]])
array([1])
>>> clf.predict([[146,0]])
array([1])
>>> 
