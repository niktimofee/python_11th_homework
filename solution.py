# 📍 Дана функция f(x) = -12x^4 - 18x^3+5x^2 + 10x - 30

# 📝 Определить корни

from sympy import *

x = Symbol('x')
func=-12*x**4+18*x**3+5*x**2+10*x-30
y=solve(func)
x1=float(y[0])
x2=float(y[1])
print(x1,x2)

# 📝 Найти интервалы, на которых функция возрастает

fd=diff(func)
print(solve(0<fd))

# 📝 Найти интервалы, на которых функция убывает

print(solve(fd<0))

# 📝 Построить график

import matplotlib.pyplot as plt
list_y=[]
for i in range(-5,6):
    x=i
    y=-12*x**4+18*x**3+5*x**2+10*x-30
    list_y.append(y)
print(list_y)
plt.plot(range(-5,6),[0,0,0,0,0,0,0,0,0,0,0])
plt.plot(range(-5,6),list_y)

# 📝 Вычислить вершину

radixs=solve(fd)
top=radixs[0]
x=top
y=-12*x**4+18*x**3+5*x**2+10*x-30
print(top,y)

# 📝 Определить промежутки, на котором f > 0

solve(0<func)

# 📝 Определить промежутки, на котором f < 0

solve(func<0)