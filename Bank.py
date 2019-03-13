import pandas as pd
from keras import Sequential
from keras.callbacks import EarlyStopping
from keras.layers import Dense

dataset = pd.read_csv("csv/boolean_bank.csv", sep=',').to_numpy()

X, Y = dataset[:, 0:20], dataset[:, 20]

model = Sequential()
model.add(Dense(40, input_dim=20, activation='relu', kernel_initializer='random_uniform'))
model.add(Dense(20, activation='relu', kernel_initializer='random_uniform'))
model.add(Dense(1, activation='sigmoid', kernel_initializer='random_uniform'))

model.compile(loss="binary_crossentropy", optimizer="adam", metrics=['accuracy'])

model.fit(X, Y, epochs=1000, batch_size=32)

scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1] * 100))

model.save('bank_model.h5')