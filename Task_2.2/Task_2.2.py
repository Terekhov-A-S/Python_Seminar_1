# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве

def LengthOfTheSegment (a, b):
    length = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)
    return length
def Coordinates(x):
    arrNum = ["x", "y"]
    num = []
    for count in range(x):
        check = False
        while not check:
            try:
                number = int(input(f"Введите координаты оси {arrNum [count]}: "))
                num.append(number)
                check = True
            except ValueError:
                print("Ошибка! Введены неверные координаты")
    return num
print("* КООРДИНАТЫ ТОЧКИ А *")
a = Coordinates (2)
print("* КООРДИНАТЫ ТОЧКИ В *")
b = Coordinates (2)
print(f"Длина указанного отрезка равна {format(LengthOfTheSegment (a, b), '.2f')}")