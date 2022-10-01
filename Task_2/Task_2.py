# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится)

def Input_print(x):
    num = [0] * x
    for i in range(x):
        check = False
        while not check:
            try:
                number = float(input(f"Введите значение координаты {i+1}: "))
                num [i] = number
                check = True
                if num [i] == 0:
                    check = False
                    print("Ошибка! X ≠ 0 и Y ≠ 0!")
            except ValueError:
                print("Ошибка! Значения координат не должны быть буквами или знаками")
    return num
def Verification (num):
    text = 4
    if num [0] > 0 and num [1] > 0:
        text = 1
    elif num [0] < 0 and num [1] > 0:
        text = 2
    elif num [0] < 0 and num [1] < 0:
        text = 3
    print(f"Точка с указанными координатами находится в {text} четверти плоскости")
koordinate = Input_print(2)
Verification (koordinate)