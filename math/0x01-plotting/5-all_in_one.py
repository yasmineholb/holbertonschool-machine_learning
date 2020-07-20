#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(constrained_layout = True)
plt.suptitle('All in one')
gs = fig.add_gridspec(3, 2)

mean = [69, 0]
cov = [[15, 8], [8, 5]]
np.random.seed(5)
x, y = np.random.multivariate_normal(mean, cov, 2000).T
y += 180
f2 = fig.add_subplot(gs[0, 1])
f2.set_title('Men\'s Height vs Weight', fontsize = 'x-small')
plt.ylabel('Weight (lbs)', fontsize = 'x-small')
plt.xlabel('Height (in)', fontsize = 'x-small')
f2.plot(x, y, 'm.')







x = np.arange(0, 28651, 5730)
r = np.log(0.5)
t = 5730
y = np.exp((r / t) * x)
f3 = fig.add_subplot(gs[1, 0])
f3.set_title('Exponential Decay of C-14', fontsize = 'x-small')
plt.yscale('log')
plt.xlim(0, 28650)
plt.ylabel('Fraction Remaining', fontsize = 'x-small')
plt.xlabel('Time (years)', fontsize = 'x-small')
f3.plot(x, y)


x1 = np.arange(0, 21000, 1000)
r1 = np.log(0.5)
t1 = 5730
t2 = 1600
y1 = np.exp((r1 / t1) * x1)
y2 = np.exp((r1 / t2) * x1)
f4 = fig.add_subplot(gs[1, 1])
f4.set_title('Exponential Decay of Radioactive Elements', fontsize = 'x-small')
plt.xlim(0 ,20000)
plt.ylim(0, 1)
plt.ylabel('Fraction Remaining', fontsize = 'x-small')
plt.xlabel('Time (years)', fontsize = 'x-small')
plt.plot(x1, y2, 'g', label='Ra-226')
plt.plot(x1, y1, 'r--', label='C-14')
plt.legend()


y = np.arange(0, 11) ** 3
f1 = fig.add_subplot(gs[0, 0])
plt.xlim([0, 10])
f1.plot(y, 'red')



f5 = fig.add_subplot(gs[2, :])
np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)
f5.set_title('Project A', fontsize = 'x-small')
plt.ylabel('Number of Students', fontsize = 'x-small')
plt.xlabel('Grades', fontsize = 'x-small')
plt.axis([0 ,100, 0, 30])
x2 = np.arange(0, 110, 10)
bn = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
plt.hist(student_grades, edgecolor="black", bins = bn)
plt.xticks(x2)
plt.show()



