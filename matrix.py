import tensorflow as tf

# 常亮矩阵
mat0 = tf.constant([[0, 0, 0], [0, 0, 0]])
# 填充为0的矩阵
mat1 = tf.zeros([2, 3])
# 填充为1的矩阵
mat2 = tf.ones([3, 2])
# 自定义填充的矩阵
mat3 = tf.fill([2, 3], 15)
with tf.Session() as sess:
    print(sess.run(mat0))
    print(sess.run(mat1))
    print(sess.run(mat2))
    print(sess.run(mat3))
