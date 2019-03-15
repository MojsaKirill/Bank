import numpy
import pandas as pd
import tensorflow as tf
import time

start_time = time.time()

dataset = pd.read_csv("csv/boolean_bank.csv", sep=',').to_numpy()

numpy.random.shuffle(dataset)

X, Y = dataset[:, 0:20], dataset[:, 20]

X = X.reshape((X.shape[0], 1, X.shape[1]))

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.LSTM(20, input_shape=(X.shape[1], X.shape[2]), return_sequences=True))
model.add(tf.keras.layers.LSTM(40, return_sequences=True))
model.add(tf.keras.layers.LSTM(80, return_sequences=True))
model.add(tf.keras.layers.LSTM(160, return_sequences=True))
model.add(tf.keras.layers.LSTM(80, return_sequences=True))
model.add(tf.keras.layers.LSTM(40, return_sequences=True))
model.add(tf.keras.layers.LSTM(20, return_sequences=True))
model.add(tf.keras.layers.LSTM(10, return_sequences=True))
model.add(tf.keras.layers.LSTM(5))
model.add(tf.keras.layers.Dense(1, activation='sigmoid', kernel_initializer='random_uniform'))
model.compile(loss="binary_crossentropy", optimizer="adam", metrics=['accuracy'])

model.fit(X, Y, epochs=1000, batch_size=2048)

scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1] * 100))

model.save('LSTM_Bank_model.h5')

print(time.time()-start_time)