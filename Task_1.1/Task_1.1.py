# Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.

def NumInput (inputText):
    check = False
    while not check:
        try:
            number = int(input(f"{inputText}"))
            check = True
        except ValueError:
            print("Вы ввели неверные данные!")
    return number
def NumCheck (num):
    if 6 <= num <= 7:
        print("Это выходной день")
    elif 0 < num < 6:
        print("Это будни")
    else:
        print("Под данным номером дней недели не существует")
num = NumInput ("Введите число, обозначающее день недели: ")
NumCheck (num)