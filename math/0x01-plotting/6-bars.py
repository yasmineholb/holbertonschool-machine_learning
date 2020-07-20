#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4,3))
plt.ylim(0, 80)
N=3
y1=[3,25,22]
y2=[9,27,27]
y3=[16,30, 29]
y4=[18,30,39.5]
xvalues = np.arange(N)

plt.bar(xvalues,y1,color='r', label ='apples')
plt.bar(xvalues,y2, color='yellow', bottom =y1, label = 'bananas')
plt.bar(xvalues,y3, color='orange', bottom =y2, label = 'oranges')
plt.bar(xvalues,y4, color='#ffe5b4', bottom =y3, label = 'peaches')
plt.xticks(xvalues, ('Farrah', 'Fred', 'Felicia'))
plt.ylabel('Quantity of Fruit')
plt.title('Number of Fruit per Person')
plt.legend()
plt.show()
