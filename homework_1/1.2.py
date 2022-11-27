#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
xyz = ['X', 'Y', 'Z']
array_num = []
for i in xyz:
    array_num.append(input(f'Введите значение {i}: '))

left = not (array_num[0] or array_num[1] or array_num[2])
right = not array_num[0] and not array_num[1] and not array_num[2]
result = left == right

if result == True:
    print('Утверждение истинно')
else:
    print('Утверждение ложно')