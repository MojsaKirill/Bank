import pandas as pd
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model

dataset = pd.read_csv("csv/boolean_bank_test.csv", sep=',').to_numpy()

X, Y = dataset[:, 0:22], dataset[:, 22]

loss_dir = ['loss_positive', 'loss_negative', 'all', "correct"]

model = load_model('bank_model.h5')

arr = model.predict(X)

loss_positive = 0
loss_negative = 0

for i in range(len(arr)):
    if arr[i] > 0.5 and Y[i]==0:
        loss_positive += 1
    if arr[i] < 0.5 and Y[i]==1:
        loss_negative += 1

print("Сверточная нейросеть")
print("Ложноположительные ошибки: ", loss_positive, " Ложноотрицательные ошибки: ", loss_negative)

loss = [loss_positive, loss_negative, len(X), len(X)-loss_positive-loss_negative]

model = load_model('LSTM_Bank_model.h5')

X = X.reshape((X.shape[0], 1, X.shape[1]))

arr = model.predict(X)

loss_positive_lstm = 0
loss_negative_lstm = 0

for i in range(len(arr)):
    if arr[i] > 0.5 and Y[i]==0:
        loss_positive_lstm += 1
    if arr[i] < 0.5 and Y[i]==1:
        loss_negative_lstm += 1

print("LSTM")
print("Ложноположительные ошибки: ", loss_positive_lstm, " Ложноотрицательные ошибки: ", loss_negative_lstm)

loss_lstm = [loss_positive, loss_negative, len(X), len(X)-loss_positive-loss_negative]

plt.figure(figsize=(20, 8))
ax =plt.subplot(131)
plt.title('Сверточная нейросеть')
plt.bar(loss_dir, loss)
plt.subplot(132)
plt.title('LSTM')
plt.bar(loss_dir, loss_lstm)
plt.show()
