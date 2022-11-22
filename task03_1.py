# Напишите программу, которая по заданному номеру четверти
# показывает диапазон возможных координат точек в этой четверти (x и y).
coordinateQuarter = int(
    input("Введите номер координатной четверти для точки "))

if coordinateQuarter == 1:
    print("Координаты X > 0 и Y > 0")
elif coordinateQuarter == 2:
    print("Координаты X < 0 и Y > 0")
elif coordinateQuarter == 3:
    print("Координаты X < 0 и Y < 0")
elif coordinateQuarter == 4:
    print("Координаты X > 0 и Y < 0")
else:
    print("Ошибка. Введён некорректный номер координатной четверти.")
