import numpy
import pandas as pd
from keras import Sequential
from keras.layers import LSTM, Dense

dataset = pd.read_csv("csv/boolean_bank.csv", sep=',').to_numpy()

numpy.random.shuffle(dataset)

X, Y = dataset[:, 0:20], dataset[:, 20]

X = X.reshape((X.shape[0], 1, X.shape[1]))

model = Sequential()
model.add(LSTM(128, input_shape=(X.shape[1], X.shape[2])))
model.add(Dense(1, activation='sigmoid', kernel_initializer='random_uniform'))

model.compile(loss="binary_crossentropy", optimizer="adam", metrics=['accuracy'])

model.fit(X, Y, epochs=1000, batch_size=32)

scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1] * 100))

model.save('LSTM_Bank_model.h5')