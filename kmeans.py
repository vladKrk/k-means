import numpy as np

#--------------------
#Меняя первые три константы получаем разные результаты
COUNT_OF_CLASTERS = 3 #Количество кластеров
N = 5 #Количество точек
M = 5 #Размерность пространства
#--------------------
MAX_ITERATIONS = 100 
#--------------------

#Генерируем набор случайных точек размерности N x M
X = np.random.rand(N, M)

#Генерируем набор точек кластеров размерности C x M
Y = np.random.rand(COUNT_OF_CLASTERS, M)
print("----------------------------------")
print("Начальные центры кластеров: ", Y)
it = 0
while it < MAX_ITERATIONS:
    NEW_CENTERS = np.zeros((COUNT_OF_CLASTERS, M)) #Новые центры кластеров
    POINTS_IN_CLASTER = np.zeros(COUNT_OF_CLASTERS) #Количество точек в каждом кластере

    for i, pointX in enumerate(X):
        Min = -1
        minIndex = -1
        for index, pointY in enumerate(Y):
            dist = np.sqrt(np.sum((pointX - pointY)**2)) 
            if(minIndex == -1):
                Min = dist
                minIndex = index
            else:
                if Min > dist:
                    Min = dist
                    minIndex = index
        #Добавляем точку к определенному центру
        NEW_CENTERS[minIndex] += X[i]
        #Увеличиваем количество точек в данном кластере на 1 
        POINTS_IN_CLASTER[minIndex] += 1
    #Для каждого кластера делим сумму точек на их количество
    for index, center in enumerate(NEW_CENTERS):
        if(POINTS_IN_CLASTER[index] != 0):
            NEW_CENTERS[index] = center / POINTS_IN_CLASTER[index]
        else:
            #Если в кластере нет точек, просто оставляем его центр начальным
            NEW_CENTERS[index] = Y[index]
    #Меняем центры кластеров на новые
    Y = NEW_CENTERS.copy()
    it += 1

print("----------------------------------")
print("Конечные центры кластеров: ", Y)