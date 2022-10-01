# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def Predicatum(x):
    side1 = not (x[0] or x[1] or x[2])
    side2 = not x[0] and not x[1] and not x[2]
    result = side1 == side2
    return result
def inputNumbers(x):
    coordinates = ["x", "y", "z"]
    a = []
    for i in range(x):
        a.append(input(f"Введите значение {coordinates [i]}: "))
    return a
print (f"Проверим истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z")
veracity = inputNumbers(3)
if Predicatum(veracity) == True:
    print(f"*Указанное утверждение истинно*")
else:
    print(f"*Указанное утверждение ложно*")