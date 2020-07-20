#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4,3))
plt.ylim(0, 80)
N=3
c=['r','yellow','orange','#ffe5b4']
l=['apples','bananas','oranges','peaches']
xvalues = np.arange(N)
plt.bar(xvalues,fruit[0,:], color=c[0], label = l[0],width=0.5)
for i in range(3):
    plt.bar(xvalues,fruit[i+1,:], color=c[i+1], bottom =fruit[i,:], label = l[i+1],width=0.5)
plt.xticks(xvalues, ('Farrah', 'Fred', 'Felicia'))
plt.ylabel('Quantity of Fruit')
plt.title('Number of Fruit per Person')
plt.legend()
plt.show()
