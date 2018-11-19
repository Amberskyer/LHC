import tensorflow as tf

data1 = tf.constant(2, dtype=tf.int32)
data2 = tf.Variable(10, name='var')

# sess = tf.Session()
# print(sess.run(data1))
# init = tf.global_variables_initializer()
# sess.run(init)
# print(sess.run(data2))
# sess.close()

# init = tf.global_variables_initializer()
# sess = tf.Session()
# with sess:
#     sess.run(init)
#     print(sess.run(data1))
#     print(sess.run(data2))

data3 = tf.constant(6)
data4 = tf.Variable(2)
dataAdd = tf.add(data3, data4)
dataCopy = tf.assign(data4, dataAdd)
dataMul = tf.multiply(data3, data4)
dataSub = tf.subtract(data3, data4)
dataDiv = tf.divide(data3, data4)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run(data1))
    print(sess.run(data2))
    print(sess.run(data3))
    print(sess.run(data4))
    print(sess.run(dataAdd))
    print(sess.run(dataMul))
    print(sess.run(dataSub))
    print(sess.run(dataDiv))
print('end')
