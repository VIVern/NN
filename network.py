# import numpy as np
# import tensorflow as tf
# from tensorflow.keras import layers
#
# model = tf.keras.Sequential()
#
# model.add(layers.Dense(3, activation='sigmoid'))
# model.add(layers.Dense(2, activation='sigmoid'))
# model.add(layers.Dense(1, activation='sigmoid'))
#
# model.compile(optimizer=tf.train.GradientDescentOptimizer(0.03),
#               loss='mse',
#               metrics=['mae'])
#
# data = np.array(
#     [
#         [0, 0, 0],
#         [1, 0, 0],
#         [0, 1, 1],
#         [1, 1, 0],
#         [1, 1, 1],
#     ],
#     int)
#
# labels = np.array(
#     [
#         [0],
#         [1],
#         [1],
#         [0],
#         [1],
#     ],
#     int)
#
#
# model.fit(data, labels, epochs=40000)
#
# result1 = model.predict(np.array([[1, 0, 0]], int))
# result2 = model.predict(np.array([[0, 1, 0]], int))
# result3 = model.predict(np.array([[0, 0, 1]], int))
# result4 = model.predict(np.array([[1, 1, 0]], int))
# result5 = model.predict(np.array([[1, 0, 1]], int))
# result6 = model.predict(np.array([[0, 1, 1]], int))
# result7 = model.predict(np.array([[1, 1, 1]], int))
# print(result1)
# print(result2)
# print(result3)
# print(result4)
# print(result5)
# print(result6)
# print(result7)


def sayHi():
    return "Hi"

