"""Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных"""

with open('homework_5\RLE.txt', 'r') as data:
    string = data.readline()

def encode(decod_str):
    encoded_string = ''
    count = 1
    char = decod_str[0]
    for i in range(1, len(decod_str)):
        if decod_str[i] == char:
            count += 1
        else:
            encoded_string = encoded_string + str(count) + char
            char = decod_str[i]
            count = 1
            encoded_string = encoded_string + str(count) + char
    return encoded_string

def decode(encod_str):
    decoded_string = ''
    char_amount = ''
    for i in range(len(encod_str)):
        if encod_str[i].isdigit():
            char_amount += encod_str[i]
        else:
            decoded_string += encod_str[i] * int(char_amount)
        char_amount = ''
    print(decoded_string)

    return decoded_string

with open('homework_5\RLE.txt', 'r') as data:
    decod_str = data.read()

with open('homework_5\encod.txt', 'w') as data:
    encod_str = encode(decod_str)
    data.write(encod_str)

print('Decoded: ' + decod_str)
print('Encoded: ' + encode(decod_str))