import tensorflow as tf

# 常亮矩阵
data1 = tf.constant([
    [6, 3],
    [6, 3],
    [6, 0]
])
data2 = tf.constant([
    [1, 5, 4, 0],
    [2, 5, 4, 0]
])
data3 = tf.constant([[3, 3]])
data4 = tf.constant([
    [1, 2],
    [3, 4],
    [5, 6]
])
data5 = tf.constant([1, 2, 3, 4, 5, 6], shape=[2, 3])

data6 = tf.constant([7, 8, 9, 10, 11, 12], shape=[3, 2])

# 填充为0的矩阵
matMul = tf.matmul(data1, data2)
matMul2 = tf.matmul(data5, data6)
# 填充为1的矩阵
matAdd = tf.add(data1, data3)
with tf.Session() as sess:
    print(sess.run(data1))
    print(sess.run(data2))
    print(sess.run(matMul))
    print(sess.run(data5))
    print(sess.run(data6))
    print(sess.run(matMul2))
    print(sess.run(matAdd))
