from sklearn.datasets import load_iris
iris = load_iris()
print iris.feature_names
iris.feature_names
iris.target_names
iris.data
iris.target
for i in range(len(iris.target)):
	print("Example %d: label %s, features %s" % (i, iris.target[i], iris.data[i]))

import numpy as np
from sklearn.datasets import load_iris
iris = load_iris()
test_idx = [0,50,100]
#training data
train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data, test_idx, axis=0)
 
#testing data
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]
from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)
DecisionTreeClassifier(class_weight=None, criterion='gini', max_depth=None,
            max_features=None, max_leaf_nodes=None,
            min_impurity_split=1e-07, min_samples_leaf=1,
            min_samples_split=2, min_weight_fraction_leaf=0.0,
            presort=False, random_state=None, splitter='best')
print(test_target)
print(clf.predict(test_data))
#viz code
from sklearn.externals.six import StringIO
import pydot
dot_data = StringIO()
tree.export_graphviz(clf,
		     out_file=dot_data,
		     feature_names=iris.feature_names,
		     class_names=iris.target_names,
		     filled=True, rounded=True,
		     impurity=False
print(test_data[0], test_target[0])
[ 5.1  3.5  1.4  0.2] 0
print(iris.feature_names, iris.target_names)
['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)'] ['setosa' 'versicolor' 'virginicaprint(test_data[1], test_target[1])
[ 7.   3.2  4.7  1.4] 1
print(test_data[2], test_target[2])
[ 6.3  3.3  6.   2.5] 2
import pydotplus
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())

