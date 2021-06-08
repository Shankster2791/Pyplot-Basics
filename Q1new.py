#Q1. Plot tan(x), cot(x), sec(x) and cosec(x) for the values of x= [-pi,-pi/4, -pi/2, 0, pi/4, pi/2, pi].

import matplotlib.pyplot as plt
import numpy as np

X = [-np.pi, -np.pi/4, -np.pi/2, 0 ,np.pi/4,np.pi/2,np.pi]

T = np.tan(X)
Cot = np.arctan(X)
Sec = np.arccos(X)
Cosec = np.arcsin(X)

plot3 = plt.figure("tan")
plt.plot(X, T, color="blue",marker = "o")
plot4 = plt.figure("Cot")
plt.plot(X, Cot, color="red",marker = "o")
plot5 = plt.figure("Sec")
plt.plot(X, Sec, color="green",marker = "o")
plot6 = plt.figure("Cosec")
plt.plot(X, Cosec, color="yellow",marker = "o")
plt.show()