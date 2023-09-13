import matplotlib.pyplot
import numpy as np
import matplotlib.pyplot as plt

plt.title('Заданеие 2')

plt.xlabel('Значение Х1')
plt.ylabel('Значение X2')

plt.xlim(-1,10)
plt.ylim(-1,10)

X = [-1, 7]
Y = [7, -1]
plt.plot(X, Y)

Y = [-1, 100]
X = [3, 3]
plt.plot(X, Y)

Y = [0, 0]
X = [-1, 100]
plt.plot(X, Y)

X = [3, 10]
Y = [0, 4.5]
plt.plot(X, Y)


X = [-1, 9.1]
Y = [(2/3)+5.3, -1]
plt.plot(X, Y)

plt.arrow(0, 0, 2, 3, width= 0.15)

plt.text(0.2, 7, 'x1 +x2 <= 6',fontsize=13)
plt.text(1, 0.7, 'Z(3,2)',fontsize=13)
plt.text(6, 3.7, 'x1 -2x2 <=3',fontsize=13)
plt.text(3.2, 6, 'x1>=3',fontsize=13)
plt.text(0, -0.7, 'x2>=0',fontsize=13)
#plt.legend(('sin','cos', "a", "aa", "aaa"))

plt.grid()

#plt.plot(X,Y)
plt.show()

#Плуталова Е.Д.
#Диденко Т.С.
#Солдатова М.С.
#номер группы: 7
