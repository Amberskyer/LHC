import tensorflow as tf

data1 = tf.placeholder(tf.int32)
data2 = tf.placeholder(tf.int32)
dataAdd = tf.add(data1, data2)
with tf.Session() as sess:
    print(sess.run(dataAdd, feed_dict={data1: 6, data2: 2}))
print('end')
