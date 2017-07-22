Python 3.5.3 (v3.5.3:1880cb95a742, Jan 16 2017, 16:02:32) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import tensorflow as tf
>>> node1 = tf.constant(3.0, dtype=tf.float32)
>>> node2 = tf.constant(4.0)
>>> print(node1, node2)
Tensor("Const:0", shape=(), dtype=float32) Tensor("Const_1:0", shape=(), dtype=float32)
>>> sess = tf.Session()
>>> print(sess.run([node1, node2]))
[3.0, 4.0]
>>> node3 = tf.add(node1, node2)
>>> print("node3: ", node3)
node3:  Tensor("Add:0", shape=(), dtype=float32)
>>> print("sess.run(node3): ", sess.run(node3))
sess.run(node3):  7.0
>>> a= tf.placeholder(tf.float32)
>>> b= tf.placeholder(tf.float32)
>>> adder_node = a+b
>>> print(sess.run(adder_node, {a: 3, b:4.5}))
7.5
>>> print(sess.run(adder_node, {a: [1,3], b:[2,4]}))
[ 3.  7.]
>>> add_and_triple = adder_node *3.
>>> print(sess.run(add_and_triple, {a:3, b:4.5}))
22.5
>>> W= tf.Variable([.3], dtype=tf.float32)
>>> b= tf.Variable([-.3], dtype=tf.float32)
>>> x= tf.placeholder(tf.float32)
>>> linear_model = W * x + b
>>> init = tf.global_variables_initializer()
>>> sess.run(init)
>>> print(sees.run(linear_model, {x:[1,2,3,4]}))
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    print(sees.run(linear_model, {x:[1,2,3,4]}))
NameError: name 'sees' is not defined
>>> print(sess.run(linear_model, {x:[1,2,3,4]}))
[ 0.          0.30000001  0.60000002  0.90000004]
>>> y = tf.placeholder(tf.float32)
>>> squared_deltas = tf.square(linear_model -y)
>>> loss = tf.reduce_sum(squared_deltas)
>>> print(sess.run(loss, {x:[1,2,3,4], y:[0,-1,-2,-3]}))
23.66
>>> fixW = tf.assign(W, [-1.])
>>> fixb = tf.assign(b, [1.])
>>> sess.run([fixW,fixb])
[array([-1.], dtype=float32), array([ 1.], dtype=float32)]
>>> print(sess.run(loss, {x:[1,2,3,4], y:[0,-1,-2,-3]}))
0.0
>>> optimizer = tf.train.GradientDescentOptimizer(0.01)
>>> train = optimizer.minimize(loss)
>>> sess.run(init)
>>> for i in range(1000):
	sess.run(train, {x:[1,2,3,4], y:[0,-1,-2,-3]})

	
>>> print(sess.run([W,b]))
[array([-0.9999969], dtype=float32), array([ 0.99999082], dtype=float32)]
>>> 
