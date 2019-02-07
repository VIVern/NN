import numpy as np
import tensorflow as tf
from tensorflow.keras import layers


class Network():

    def __init__(self):
        self.network = self.initialize_network()

    def initialize_network(self):
        model = tf.keras.Sequential()

        model.add(layers.Dense(1000, activation='sigmoid', input_dim=2500))
        model.add(layers.Dense(500, activation='sigmoid'))
        model.add(layers.Dense(10, activation='sigmoid'))

        model.compile(optimizer=tf.train.GradientDescentOptimizer(0.01),
                      loss='mse',
                      metrics=['mae'])

        return model

    def train_network(self, data):
        income = []
        expected = []

        for json in data:
            income.append(json['image'])
            expected.append(json['expected-vector'])

        self.network.fit(np.array(income, int), np.array(expected, int), epochs=500)

    def make_prediction(self, income_data):
        prediction = self.network.predict(np.array([income_data]))

        return prediction

    def save_weights(self):
        self.network.save_weights("model.h5")

    def load_weights(self):
        self.network.load_weights("model.h5")

