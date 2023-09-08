import matplotlib.pyplot
import numpy as np
import matplotlib.pyplot as plt

plt.title('Заданеие 1')

plt.xlabel('Значение Х1')
plt.ylabel('Значение X2')

plt.xlim(0,40)
plt.ylim(0,40)

X = [0, 28.2]
Y = [35.25, 0]
plt.plot(X, Y)

X = [0, 100]
Y = [19, 19]
plt.plot(X, Y)

X = [17, 17]
Y = [0, 100]
plt.plot(X, Y)

#X = [0, 3]
#Y = [0, 5]
#plt.plot(X, Y)


X = [0, 34/3]
Y = [34/5, 0]
plt.plot(X, Y)

plt.arrow(0, 0, 3, 5, width= 0.2)

plt.text(1.5, 1, 'Z(3,4)',fontsize=10)
plt.text(17.2, 1, 'X1 <= 17',fontsize=10)
plt.text(1.2, 19.5, 'X2 <= 19',fontsize=10)
plt.text(22, 10, '4X1 + 5X2 <= 141',fontsize=10)
#plt.legend(('sin','cos', "a", "aa", "aaa"))

plt.grid()

#plt.plot(X,Y)
plt.show()

#Плуталова Е.Д.
#Диденко Т.С.
#Солдатова М.С.
#номер группы: 7

#изменение 1