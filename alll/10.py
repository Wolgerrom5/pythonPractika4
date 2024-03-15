pin = input('Введите PIN код: ')
if len(pin) != 4:
    print('ERROR')
else:
    if len(set(pin)) != 4:
        print('ERROR')
    else:
        if 1900 <= int(pin) <= 2050:
            print('ERROR')
        else:
            print('OK')