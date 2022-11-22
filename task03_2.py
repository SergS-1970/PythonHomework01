# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import os
import math

coordinateXOfPointA = float(input('Введите координату точки А по оси Х: '))
coordinateYOfPointA = float(input('Введите координату точки А по оси Y: '))
coordinateXOfPointB = float(input('Введите координату точки B по оси Х: '))
coordinateYOfPointB = float(input('Введите координату точки B по оси Y: '))

distance = round(math.sqrt((coordinateXOfPointB - coordinateXOfPointA)**2 + (coordinateYOfPointB - coordinateYOfPointA)**2), 2)
print(distance)