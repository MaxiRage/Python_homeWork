def info_subs ():
    info = []
    last_name = input('Введите фамилию: ')
    info.append(last_name)
    first_name = input('Введите имя: ')
    info.append(first_name)
    phone_number = ''
    valid = False
    while not valid:
        try:
            phone_number = input('Введите номер телефона: ')
            if len(phone_number) != 10:
                print('Номер должен состоять из 10 цифр начиная с 9-ки')
            else:
                phone_number = int(phone_number)
                valid = True
        except:
            print('Номер телефона содержит только цифры')
    info.append(phone_number)
    description = input('Введите описание: ')
    info.append(description)
    return info