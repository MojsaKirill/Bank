import pandas as pd
import tensorflow as tf
import time

start_time = time.time()

dataset = pd.read_csv("csv/boolean_bank.csv", sep=',').to_numpy()

X, Y = dataset[:, 0:20], dataset[:, 20]

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(40, input_dim=20, activation='relu', kernel_initializer='random_uniform'))
model.add(tf.keras.layers.Dense(20, activation='relu', kernel_initializer='random_uniform'))
model.add(tf.keras.layers.Dense(1, activation='sigmoid', kernel_initializer='random_uniform'))

model.compile(loss="binary_crossentropy", optimizer="adam", metrics=['accuracy'])

model.fit(X, Y, epochs=20, batch_size=32)

scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1] * 100))

model.save('bank_model.h5')

print(time.time()-start_time)