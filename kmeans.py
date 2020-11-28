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
    dist1 = X - Y[:, np.newaxis]
    distances = np.sqrt((dist1**2).sum(axis = 2))
    closest_centroids = np.argmin(distances, axis = 0)
    NEW_CENTERS = np.zeros((COUNT_OF_CLASTERS, M))
    COUNT_OF_POINTS = np.zeros(COUNT_OF_CLASTERS)
    for i, c in enumerate(closest_centroids):
        NEW_CENTERS[c] += X[i]
        COUNT_OF_POINTS[c] += 1

    for i in range(COUNT_OF_CLASTERS):
        if(COUNT_OF_POINTS[i] != 0):
            NEW_CENTERS[i] /= COUNT_OF_POINTS[i]
        else:
            NEW_CENTERS[i] = Y[i]
    Y = NEW_CENTERS.copy()
    it += 1

print("----------------------------------")
print("Конечные центры кластеров: ", Y)