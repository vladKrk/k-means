import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from random import random, choice

#--------------------
#Меняя первые две константы получаем разные результаты
COUNT_OF_CLASTERS = 5
NUMBER_OF_POINTS = 100

MAX_ITERATIONS = 100
#--------------------

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def update(self, x, y):
        self.x = x
        self.y = y

class Claster:
    def __init__(self, center, color):
        self.center = center
        self.color = color
        self.points = []
    def addPoint(self, a):
        self.points.append(a)
    def updateCenter(self):
        xCenter = 0
        yCenter = 0
        for point in self.points:
            xCenter += point.x
            yCenter += point.y
        self.center = Point(xCenter / len(self.points), yCenter / len(self.points))
        self.points.clear()

#--------------------

def distance(a, b):
    return (b.x - a.x) * (b.x - a.x) + (b.y - a.y) * (b.y - a.y)

#--------------------

#Генерируем набор случайных точек
x = np.random.rand(NUMBER_OF_POINTS)
y = np.random.rand(NUMBER_OF_POINTS)


clasters = []
colors = []
#Случайным образом генериоруем наши кластеры (выбираем центры и цвета)
for i in range(COUNT_OF_CLASTERS):
    while(True):
        item = choice(list(matplotlib.colors.cnames.items()))
        if(item[1] not in colors):
            break
    colors.append(item[1])
    clasters.append(Claster(Point(random(), random()), item[1]))

#Содаем окна с точками
fig1, ax1 = plt.subplots()
ax1.scatter(x, y, c = "g", edgecolors = 'black')
fig2, ax2 = plt.subplots()
ax2.scatter(x, y, c = "g", edgecolors = 'black')
#----------------------

it = 0
point = Point(0, 0)
while it < MAX_ITERATIONS:

    #Обновляем центры кластеров
    if it != 0:
        for i in range(COUNT_OF_CLASTERS):
            clasters[i].updateCenter()
    
    for i in range(NUMBER_OF_POINTS):
        Min = 9999
        minIndex = -1
        point.update(x[i], y[i])
        #Ищем ближайший к точке кластер
        for j in range(COUNT_OF_CLASTERS):
            dis = distance(clasters[j].center, point)
            if dis < Min:
                Min = dis
                minIndex = j
        #Добавляем к найденому кластеру точку
        clasters[minIndex].addPoint(Point(x[i], y[i]))
    it += 1

#В итоге просто отрисовываем точки каждого кластера в своем цвете
for i in range(COUNT_OF_CLASTERS):
    for point in clasters[i].points:
        ax2.scatter(point.x, point.y, c = clasters[i].color, edgecolors = 'black')
    #Тут также нарисуем центры кластеров
    ax2.scatter(clasters[i].center.x, clasters[i].center.y, s = 80, c = 'black', edgecolors = 'red')

plt.show()
