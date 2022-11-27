#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

array_num = [input(f'Введите значение X: '), input(f'Введите значение Y: '), input(f'Введите значение Z: ')]

left = not (array_num[0] or array_num[1] or array_num[2])
right = not array_num[0] and not array_num[1] and not array_num[2]
result = left == right

if result == True:
    print('Утверждение истинно')
else:
    print('Утверждение ложно')