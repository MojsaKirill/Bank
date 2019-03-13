import matplotlib.pyplot as plt

names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

plt.subplot(131)
plt.bar(names, values)
plt.show()