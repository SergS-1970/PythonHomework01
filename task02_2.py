# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
axisCoordinateX = int(input("Введите координату точки по оси X "))
axisCoordinateY = int(input("Введите координату точки по оси Y "))

if axisCoordinateX == 0 or axisCoordinateY == 0:
    print("Ошибка! Точка лежит на координатной оси.")
elif axisCoordinateX > 0 and axisCoordinateY > 0:
    print("Точка находится в четверти 1")
elif axisCoordinateX < 0 and axisCoordinateY < 0:
    print("Точка находится в четверти 3")
elif axisCoordinateX > 0:
    print("Точка находится в четверти 4")
elif axisCoordinateY > 0:
    print("Точка находится в четверти 2")
