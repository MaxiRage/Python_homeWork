"""Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных"""

with open('homework_5\RLE.txt', 'r') as data:
    text = data.read()

def encode_rle(text):
    code = ''
    prev = ''
    count = 1
    for char in text:
        if char != prev:
            if prev:
                code += str(count) + prev
            count = 1
            prev = char
        else:
            count += 1
    return code
          
code = encode_rle(text)
print(code)
dev = code

with open('homework_5\encod.txt', 'w') as data:
    data.write(dev)