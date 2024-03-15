pin = input('Введите PIN код: ')
if len(pin) != 4:
    print('ERROR')
else:
    if len(set(pin)) != 4:
        print('ERROR')
    else:
        # Проверка на год рождения
        if int(pin) >= 1900 and int(pin) <= 2050:
            print('ERROR')
        else:
            print('OK')