Python 3.5.3 (v3.5.3:1880cb95a742, Jan 16 2017, 16:02:32) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from sklearn.datasets import load_iris
>>> iris = load_iris()
>>> print iris.feature_names
SyntaxError: Missing parentheses in call to 'print'
>>> iris.feature_names
['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
>>> iris.target_names
array(['setosa', 'versicolor', 'virginica'], 
      dtype='<U10')
>>> iris.data
array([[ 5.1,  3.5,  1.4,  0.2],
       [ 4.9,  3. ,  1.4,  0.2],
       [ 4.7,  3.2,  1.3,  0.2],
       [ 4.6,  3.1,  1.5,  0.2],
       [ 5. ,  3.6,  1.4,  0.2],
       [ 5.4,  3.9,  1.7,  0.4],
       [ 4.6,  3.4,  1.4,  0.3],
       [ 5. ,  3.4,  1.5,  0.2],
       [ 4.4,  2.9,  1.4,  0.2],
       [ 4.9,  3.1,  1.5,  0.1],
       [ 5.4,  3.7,  1.5,  0.2],
       [ 4.8,  3.4,  1.6,  0.2],
       [ 4.8,  3. ,  1.4,  0.1],
       [ 4.3,  3. ,  1.1,  0.1],
       [ 5.8,  4. ,  1.2,  0.2],
       [ 5.7,  4.4,  1.5,  0.4],
       [ 5.4,  3.9,  1.3,  0.4],
       [ 5.1,  3.5,  1.4,  0.3],
       [ 5.7,  3.8,  1.7,  0.3],
       [ 5.1,  3.8,  1.5,  0.3],
       [ 5.4,  3.4,  1.7,  0.2],
       [ 5.1,  3.7,  1.5,  0.4],
       [ 4.6,  3.6,  1. ,  0.2],
       [ 5.1,  3.3,  1.7,  0.5],
       [ 4.8,  3.4,  1.9,  0.2],
       [ 5. ,  3. ,  1.6,  0.2],
       [ 5. ,  3.4,  1.6,  0.4],
       [ 5.2,  3.5,  1.5,  0.2],
       [ 5.2,  3.4,  1.4,  0.2],
       [ 4.7,  3.2,  1.6,  0.2],
       [ 4.8,  3.1,  1.6,  0.2],
       [ 5.4,  3.4,  1.5,  0.4],
       [ 5.2,  4.1,  1.5,  0.1],
       [ 5.5,  4.2,  1.4,  0.2],
       [ 4.9,  3.1,  1.5,  0.1],
       [ 5. ,  3.2,  1.2,  0.2],
       [ 5.5,  3.5,  1.3,  0.2],
       [ 4.9,  3.1,  1.5,  0.1],
       [ 4.4,  3. ,  1.3,  0.2],
       [ 5.1,  3.4,  1.5,  0.2],
       [ 5. ,  3.5,  1.3,  0.3],
       [ 4.5,  2.3,  1.3,  0.3],
       [ 4.4,  3.2,  1.3,  0.2],
       [ 5. ,  3.5,  1.6,  0.6],
       [ 5.1,  3.8,  1.9,  0.4],
       [ 4.8,  3. ,  1.4,  0.3],
       [ 5.1,  3.8,  1.6,  0.2],
       [ 4.6,  3.2,  1.4,  0.2],
       [ 5.3,  3.7,  1.5,  0.2],
       [ 5. ,  3.3,  1.4,  0.2],
       [ 7. ,  3.2,  4.7,  1.4],
       [ 6.4,  3.2,  4.5,  1.5],
       [ 6.9,  3.1,  4.9,  1.5],
       [ 5.5,  2.3,  4. ,  1.3],
       [ 6.5,  2.8,  4.6,  1.5],
       [ 5.7,  2.8,  4.5,  1.3],
       [ 6.3,  3.3,  4.7,  1.6],
       [ 4.9,  2.4,  3.3,  1. ],
       [ 6.6,  2.9,  4.6,  1.3],
       [ 5.2,  2.7,  3.9,  1.4],
       [ 5. ,  2. ,  3.5,  1. ],
       [ 5.9,  3. ,  4.2,  1.5],
       [ 6. ,  2.2,  4. ,  1. ],
       [ 6.1,  2.9,  4.7,  1.4],
       [ 5.6,  2.9,  3.6,  1.3],
       [ 6.7,  3.1,  4.4,  1.4],
       [ 5.6,  3. ,  4.5,  1.5],
       [ 5.8,  2.7,  4.1,  1. ],
       [ 6.2,  2.2,  4.5,  1.5],
       [ 5.6,  2.5,  3.9,  1.1],
       [ 5.9,  3.2,  4.8,  1.8],
       [ 6.1,  2.8,  4. ,  1.3],
       [ 6.3,  2.5,  4.9,  1.5],
       [ 6.1,  2.8,  4.7,  1.2],
       [ 6.4,  2.9,  4.3,  1.3],
       [ 6.6,  3. ,  4.4,  1.4],
       [ 6.8,  2.8,  4.8,  1.4],
       [ 6.7,  3. ,  5. ,  1.7],
       [ 6. ,  2.9,  4.5,  1.5],
       [ 5.7,  2.6,  3.5,  1. ],
       [ 5.5,  2.4,  3.8,  1.1],
       [ 5.5,  2.4,  3.7,  1. ],
       [ 5.8,  2.7,  3.9,  1.2],
       [ 6. ,  2.7,  5.1,  1.6],
       [ 5.4,  3. ,  4.5,  1.5],
       [ 6. ,  3.4,  4.5,  1.6],
       [ 6.7,  3.1,  4.7,  1.5],
       [ 6.3,  2.3,  4.4,  1.3],
       [ 5.6,  3. ,  4.1,  1.3],
       [ 5.5,  2.5,  4. ,  1.3],
       [ 5.5,  2.6,  4.4,  1.2],
       [ 6.1,  3. ,  4.6,  1.4],
       [ 5.8,  2.6,  4. ,  1.2],
       [ 5. ,  2.3,  3.3,  1. ],
       [ 5.6,  2.7,  4.2,  1.3],
       [ 5.7,  3. ,  4.2,  1.2],
       [ 5.7,  2.9,  4.2,  1.3],
       [ 6.2,  2.9,  4.3,  1.3],
       [ 5.1,  2.5,  3. ,  1.1],
       [ 5.7,  2.8,  4.1,  1.3],
       [ 6.3,  3.3,  6. ,  2.5],
       [ 5.8,  2.7,  5.1,  1.9],
       [ 7.1,  3. ,  5.9,  2.1],
       [ 6.3,  2.9,  5.6,  1.8],
       [ 6.5,  3. ,  5.8,  2.2],
       [ 7.6,  3. ,  6.6,  2.1],
       [ 4.9,  2.5,  4.5,  1.7],
       [ 7.3,  2.9,  6.3,  1.8],
       [ 6.7,  2.5,  5.8,  1.8],
       [ 7.2,  3.6,  6.1,  2.5],
       [ 6.5,  3.2,  5.1,  2. ],
       [ 6.4,  2.7,  5.3,  1.9],
       [ 6.8,  3. ,  5.5,  2.1],
       [ 5.7,  2.5,  5. ,  2. ],
       [ 5.8,  2.8,  5.1,  2.4],
       [ 6.4,  3.2,  5.3,  2.3],
       [ 6.5,  3. ,  5.5,  1.8],
       [ 7.7,  3.8,  6.7,  2.2],
       [ 7.7,  2.6,  6.9,  2.3],
       [ 6. ,  2.2,  5. ,  1.5],
       [ 6.9,  3.2,  5.7,  2.3],
       [ 5.6,  2.8,  4.9,  2. ],
       [ 7.7,  2.8,  6.7,  2. ],
       [ 6.3,  2.7,  4.9,  1.8],
       [ 6.7,  3.3,  5.7,  2.1],
       [ 7.2,  3.2,  6. ,  1.8],
       [ 6.2,  2.8,  4.8,  1.8],
       [ 6.1,  3. ,  4.9,  1.8],
       [ 6.4,  2.8,  5.6,  2.1],
       [ 7.2,  3. ,  5.8,  1.6],
       [ 7.4,  2.8,  6.1,  1.9],
       [ 7.9,  3.8,  6.4,  2. ],
       [ 6.4,  2.8,  5.6,  2.2],
       [ 6.3,  2.8,  5.1,  1.5],
       [ 6.1,  2.6,  5.6,  1.4],
       [ 7.7,  3. ,  6.1,  2.3],
       [ 6.3,  3.4,  5.6,  2.4],
       [ 6.4,  3.1,  5.5,  1.8],
       [ 6. ,  3. ,  4.8,  1.8],
       [ 6.9,  3.1,  5.4,  2.1],
       [ 6.7,  3.1,  5.6,  2.4],
       [ 6.9,  3.1,  5.1,  2.3],
       [ 5.8,  2.7,  5.1,  1.9],
       [ 6.8,  3.2,  5.9,  2.3],
       [ 6.7,  3.3,  5.7,  2.5],
       [ 6.7,  3. ,  5.2,  2.3],
       [ 6.3,  2.5,  5. ,  1.9],
       [ 6.5,  3. ,  5.2,  2. ],
       [ 6.2,  3.4,  5.4,  2.3],
       [ 5.9,  3. ,  5.1,  1.8]])
>>> iris target
SyntaxError: invalid syntax
>>> iris.target
array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])
>>> for i in rang(len(iris.target)):
	print "Example %d: label %s, features %s" % (i, iris.target[i], iris.data[i])
	
SyntaxError: invalid syntax
>>> for i in rang(len(iris.target)):
	print("Example %d: label %s, features %s" % (i, iris.target[i], iris.data[i]))

	
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    for i in rang(len(iris.target)):
NameError: name 'rang' is not defined
>>> for i in range(len(iris.target)):
	print("Example %d: label %s, features %s" % (i, iris.target[i], iris.data[i]))

	
Example 0: label 0, features [ 5.1  3.5  1.4  0.2]
Example 1: label 0, features [ 4.9  3.   1.4  0.2]
Example 2: label 0, features [ 4.7  3.2  1.3  0.2]
Example 3: label 0, features [ 4.6  3.1  1.5  0.2]
Example 4: label 0, features [ 5.   3.6  1.4  0.2]
Example 5: label 0, features [ 5.4  3.9  1.7  0.4]
Example 6: label 0, features [ 4.6  3.4  1.4  0.3]
Example 7: label 0, features [ 5.   3.4  1.5  0.2]
Example 8: label 0, features [ 4.4  2.9  1.4  0.2]
Example 9: label 0, features [ 4.9  3.1  1.5  0.1]
Example 10: label 0, features [ 5.4  3.7  1.5  0.2]
Example 11: label 0, features [ 4.8  3.4  1.6  0.2]
Example 12: label 0, features [ 4.8  3.   1.4  0.1]
Example 13: label 0, features [ 4.3  3.   1.1  0.1]
Example 14: label 0, features [ 5.8  4.   1.2  0.2]
Example 15: label 0, features [ 5.7  4.4  1.5  0.4]
Example 16: label 0, features [ 5.4  3.9  1.3  0.4]
Example 17: label 0, features [ 5.1  3.5  1.4  0.3]
Example 18: label 0, features [ 5.7  3.8  1.7  0.3]
Example 19: label 0, features [ 5.1  3.8  1.5  0.3]
Example 20: label 0, features [ 5.4  3.4  1.7  0.2]
Example 21: label 0, features [ 5.1  3.7  1.5  0.4]
Example 22: label 0, features [ 4.6  3.6  1.   0.2]
Example 23: label 0, features [ 5.1  3.3  1.7  0.5]
Example 24: label 0, features [ 4.8  3.4  1.9  0.2]
Example 25: label 0, features [ 5.   3.   1.6  0.2]
Example 26: label 0, features [ 5.   3.4  1.6  0.4]
Example 27: label 0, features [ 5.2  3.5  1.5  0.2]
Example 28: label 0, features [ 5.2  3.4  1.4  0.2]
Example 29: label 0, features [ 4.7  3.2  1.6  0.2]
Example 30: label 0, features [ 4.8  3.1  1.6  0.2]
Example 31: label 0, features [ 5.4  3.4  1.5  0.4]
Example 32: label 0, features [ 5.2  4.1  1.5  0.1]
Example 33: label 0, features [ 5.5  4.2  1.4  0.2]
Example 34: label 0, features [ 4.9  3.1  1.5  0.1]
Example 35: label 0, features [ 5.   3.2  1.2  0.2]
Example 36: label 0, features [ 5.5  3.5  1.3  0.2]
Example 37: label 0, features [ 4.9  3.1  1.5  0.1]
Example 38: label 0, features [ 4.4  3.   1.3  0.2]
Example 39: label 0, features [ 5.1  3.4  1.5  0.2]
Example 40: label 0, features [ 5.   3.5  1.3  0.3]
Example 41: label 0, features [ 4.5  2.3  1.3  0.3]
Example 42: label 0, features [ 4.4  3.2  1.3  0.2]
Example 43: label 0, features [ 5.   3.5  1.6  0.6]
Example 44: label 0, features [ 5.1  3.8  1.9  0.4]
Example 45: label 0, features [ 4.8  3.   1.4  0.3]
Example 46: label 0, features [ 5.1  3.8  1.6  0.2]
Example 47: label 0, features [ 4.6  3.2  1.4  0.2]
Example 48: label 0, features [ 5.3  3.7  1.5  0.2]
Example 49: label 0, features [ 5.   3.3  1.4  0.2]
Example 50: label 1, features [ 7.   3.2  4.7  1.4]
Example 51: label 1, features [ 6.4  3.2  4.5  1.5]
Example 52: label 1, features [ 6.9  3.1  4.9  1.5]
Example 53: label 1, features [ 5.5  2.3  4.   1.3]
Example 54: label 1, features [ 6.5  2.8  4.6  1.5]
Example 55: label 1, features [ 5.7  2.8  4.5  1.3]
Example 56: label 1, features [ 6.3  3.3  4.7  1.6]
Example 57: label 1, features [ 4.9  2.4  3.3  1. ]
Example 58: label 1, features [ 6.6  2.9  4.6  1.3]
Example 59: label 1, features [ 5.2  2.7  3.9  1.4]
Example 60: label 1, features [ 5.   2.   3.5  1. ]
Example 61: label 1, features [ 5.9  3.   4.2  1.5]
Example 62: label 1, features [ 6.   2.2  4.   1. ]
Example 63: label 1, features [ 6.1  2.9  4.7  1.4]
Example 64: label 1, features [ 5.6  2.9  3.6  1.3]
Example 65: label 1, features [ 6.7  3.1  4.4  1.4]
Example 66: label 1, features [ 5.6  3.   4.5  1.5]
Example 67: label 1, features [ 5.8  2.7  4.1  1. ]
Example 68: label 1, features [ 6.2  2.2  4.5  1.5]
Example 69: label 1, features [ 5.6  2.5  3.9  1.1]
Example 70: label 1, features [ 5.9  3.2  4.8  1.8]
Example 71: label 1, features [ 6.1  2.8  4.   1.3]
Example 72: label 1, features [ 6.3  2.5  4.9  1.5]
Example 73: label 1, features [ 6.1  2.8  4.7  1.2]
Example 74: label 1, features [ 6.4  2.9  4.3  1.3]
Example 75: label 1, features [ 6.6  3.   4.4  1.4]
Example 76: label 1, features [ 6.8  2.8  4.8  1.4]
Example 77: label 1, features [ 6.7  3.   5.   1.7]
Example 78: label 1, features [ 6.   2.9  4.5  1.5]
Example 79: label 1, features [ 5.7  2.6  3.5  1. ]
Example 80: label 1, features [ 5.5  2.4  3.8  1.1]
Example 81: label 1, features [ 5.5  2.4  3.7  1. ]
Example 82: label 1, features [ 5.8  2.7  3.9  1.2]
Example 83: label 1, features [ 6.   2.7  5.1  1.6]
Example 84: label 1, features [ 5.4  3.   4.5  1.5]
Example 85: label 1, features [ 6.   3.4  4.5  1.6]
Example 86: label 1, features [ 6.7  3.1  4.7  1.5]
Example 87: label 1, features [ 6.3  2.3  4.4  1.3]
Example 88: label 1, features [ 5.6  3.   4.1  1.3]
Example 89: label 1, features [ 5.5  2.5  4.   1.3]
Example 90: label 1, features [ 5.5  2.6  4.4  1.2]
Example 91: label 1, features [ 6.1  3.   4.6  1.4]
Example 92: label 1, features [ 5.8  2.6  4.   1.2]
Example 93: label 1, features [ 5.   2.3  3.3  1. ]
Example 94: label 1, features [ 5.6  2.7  4.2  1.3]
Example 95: label 1, features [ 5.7  3.   4.2  1.2]
Example 96: label 1, features [ 5.7  2.9  4.2  1.3]
Example 97: label 1, features [ 6.2  2.9  4.3  1.3]
Example 98: label 1, features [ 5.1  2.5  3.   1.1]
Example 99: label 1, features [ 5.7  2.8  4.1  1.3]
Example 100: label 2, features [ 6.3  3.3  6.   2.5]
Example 101: label 2, features [ 5.8  2.7  5.1  1.9]
Example 102: label 2, features [ 7.1  3.   5.9  2.1]
Example 103: label 2, features [ 6.3  2.9  5.6  1.8]
Example 104: label 2, features [ 6.5  3.   5.8  2.2]
Example 105: label 2, features [ 7.6  3.   6.6  2.1]
Example 106: label 2, features [ 4.9  2.5  4.5  1.7]
Example 107: label 2, features [ 7.3  2.9  6.3  1.8]
Example 108: label 2, features [ 6.7  2.5  5.8  1.8]
Example 109: label 2, features [ 7.2  3.6  6.1  2.5]
Example 110: label 2, features [ 6.5  3.2  5.1  2. ]
Example 111: label 2, features [ 6.4  2.7  5.3  1.9]
Example 112: label 2, features [ 6.8  3.   5.5  2.1]
Example 113: label 2, features [ 5.7  2.5  5.   2. ]
Example 114: label 2, features [ 5.8  2.8  5.1  2.4]
Example 115: label 2, features [ 6.4  3.2  5.3  2.3]
Example 116: label 2, features [ 6.5  3.   5.5  1.8]
Example 117: label 2, features [ 7.7  3.8  6.7  2.2]
Example 118: label 2, features [ 7.7  2.6  6.9  2.3]
Example 119: label 2, features [ 6.   2.2  5.   1.5]
Example 120: label 2, features [ 6.9  3.2  5.7  2.3]
Example 121: label 2, features [ 5.6  2.8  4.9  2. ]
Example 122: label 2, features [ 7.7  2.8  6.7  2. ]
Example 123: label 2, features [ 6.3  2.7  4.9  1.8]
Example 124: label 2, features [ 6.7  3.3  5.7  2.1]
Example 125: label 2, features [ 7.2  3.2  6.   1.8]
Example 126: label 2, features [ 6.2  2.8  4.8  1.8]
Example 127: label 2, features [ 6.1  3.   4.9  1.8]
Example 128: label 2, features [ 6.4  2.8  5.6  2.1]
Example 129: label 2, features [ 7.2  3.   5.8  1.6]
Example 130: label 2, features [ 7.4  2.8  6.1  1.9]
Example 131: label 2, features [ 7.9  3.8  6.4  2. ]
Example 132: label 2, features [ 6.4  2.8  5.6  2.2]
Example 133: label 2, features [ 6.3  2.8  5.1  1.5]
Example 134: label 2, features [ 6.1  2.6  5.6  1.4]
Example 135: label 2, features [ 7.7  3.   6.1  2.3]
Example 136: label 2, features [ 6.3  3.4  5.6  2.4]
Example 137: label 2, features [ 6.4  3.1  5.5  1.8]
Example 138: label 2, features [ 6.   3.   4.8  1.8]
Example 139: label 2, features [ 6.9  3.1  5.4  2.1]
Example 140: label 2, features [ 6.7  3.1  5.6  2.4]
Example 141: label 2, features [ 6.9  3.1  5.1  2.3]
Example 142: label 2, features [ 5.8  2.7  5.1  1.9]
Example 143: label 2, features [ 6.8  3.2  5.9  2.3]
Example 144: label 2, features [ 6.7  3.3  5.7  2.5]
Example 145: label 2, features [ 6.7  3.   5.2  2.3]
Example 146: label 2, features [ 6.3  2.5  5.   1.9]
Example 147: label 2, features [ 6.5  3.   5.2  2. ]
Example 148: label 2, features [ 6.2  3.4  5.4  2.3]
Example 149: label 2, features [ 5.9  3.   5.1  1.8]
>>> import numpy as np
>>> from sklearn.datasets import load_iris
>>> iris = load_iris()
>>> test_idx = [0,50,100]
>>> #training data
>>> train_target = np.delete(iris.target, test_idx)
>>> train_data = np.delete(iris.data, test_idx, axis=0)
>>> 
>>> #testing data
>>> test_target = iris.target[test_idx]
>>> test_data = iris.data[test_idx]
>>> from sklearn import tree
>>> clf = tree.DecisionTreeClassifier()
>>> clf.fit(train_data)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    clf.fit(train_data)
TypeError: fit() missing 1 required positional argument: 'y'
>>> clf.fit(train_data, train_target)
DecisionTreeClassifier(class_weight=None, criterion='gini', max_depth=None,
            max_features=None, max_leaf_nodes=None,
            min_impurity_split=1e-07, min_samples_leaf=1,
            min_samples_split=2, min_weight_fraction_leaf=0.0,
            presort=False, random_state=None, splitter='best')
>>> print(test_target)
[0 1 2]
>>> print(clf.predict(test_data))
[0 1 2]
>>> #viz code
>>> from sklearn.externals.s
SyntaxError: invalid syntax
>>> 
>>> from sklearn.externals.six import StringIO
>>> import pydot
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    import pydot
ImportError: No module named 'pydot'
>>> import pydot
>>> dot_data = StringIO()
>>> tree.export_graphviz(clf,
		     out_file=dot_data,
		     feature_names=iris.feature_names,
		     class_names=iris.target_names,
		     filled=True, rounded=True,
		     impurity=False)
>>> graph = pydot.graph_from_dot_data(dot_data.getvalue())
>>> graph.write_pdf("iris.pdf")
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    graph.write_pdf("iris.pdf")
AttributeError: 'list' object has no attribute 'write_pdf'
>>> print(graph)
[<pydot.Dot object at 0x000001BA7B31CAC8>]
>>> print(dot_data.getvalue())
digraph Tree {
node [shape=box, style="filled, rounded", color="black", fontname=helvetica] ;
edge [fontname=helvetica] ;
0 [label="petal length (cm) <= 2.45\nsamples = 147\nvalue = [49, 49, 49]\nclass = setosa", fillcolor="#e5813900"] ;
1 [label="samples = 49\nvalue = [49, 0, 0]\nclass = setosa", fillcolor="#e58139ff"] ;
0 -> 1 [labeldistance=2.5, labelangle=45, headlabel="True"] ;
2 [label="petal width (cm) <= 1.75\nsamples = 98\nvalue = [0, 49, 49]\nclass = versicolor", fillcolor="#39e58100"] ;
0 -> 2 [labeldistance=2.5, labelangle=-45, headlabel="False"] ;
3 [label="petal length (cm) <= 4.95\nsamples = 53\nvalue = [0, 48, 5]\nclass = versicolor", fillcolor="#39e581e4"] ;
2 -> 3 ;
4 [label="petal width (cm) <= 1.65\nsamples = 47\nvalue = [0, 46, 1]\nclass = versicolor", fillcolor="#39e581f9"] ;
3 -> 4 ;
5 [label="samples = 46\nvalue = [0, 46, 0]\nclass = versicolor", fillcolor="#39e581ff"] ;
4 -> 5 ;
6 [label="samples = 1\nvalue = [0, 0, 1]\nclass = virginica", fillcolor="#8139e5ff"] ;
4 -> 6 ;
7 [label="petal width (cm) <= 1.55\nsamples = 6\nvalue = [0, 2, 4]\nclass = virginica", fillcolor="#8139e57f"] ;
3 -> 7 ;
8 [label="samples = 3\nvalue = [0, 0, 3]\nclass = virginica", fillcolor="#8139e5ff"] ;
7 -> 8 ;
9 [label="sepal length (cm) <= 6.95\nsamples = 3\nvalue = [0, 2, 1]\nclass = versicolor", fillcolor="#39e5817f"] ;
7 -> 9 ;
10 [label="samples = 2\nvalue = [0, 2, 0]\nclass = versicolor", fillcolor="#39e581ff"] ;
9 -> 10 ;
11 [label="samples = 1\nvalue = [0, 0, 1]\nclass = virginica", fillcolor="#8139e5ff"] ;
9 -> 11 ;
12 [label="petal length (cm) <= 4.85\nsamples = 45\nvalue = [0, 1, 44]\nclass = virginica", fillcolor="#8139e5f9"] ;
2 -> 12 ;
13 [label="sepal width (cm) <= 3.1\nsamples = 3\nvalue = [0, 1, 2]\nclass = virginica", fillcolor="#8139e57f"] ;
12 -> 13 ;
14 [label="samples = 2\nvalue = [0, 0, 2]\nclass = virginica", fillcolor="#8139e5ff"] ;
13 -> 14 ;
15 [label="samples = 1\nvalue = [0, 1, 0]\nclass = versicolor", fillcolor="#39e581ff"] ;
13 -> 15 ;
16 [label="samples = 42\nvalue = [0, 0, 42]\nclass = virginica", fillcolor="#8139e5ff"] ;
12 -> 16 ;
}
>>> print(test_data[0], test_target[0])
[ 5.1  3.5  1.4  0.2] 0
>>> print(iris.feature_names, iris.target_names)
['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)'] ['setosa' 'versicolor' 'virginica']
>>> print(test_data[1], test_target[1])
[ 7.   3.2  4.7  1.4] 1
>>> print(test_data[2], test_target[2])
[ 6.3  3.3  6.   2.5] 2
>>> 
