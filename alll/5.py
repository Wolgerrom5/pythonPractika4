height = float(input('Введите рост в сантиметрах:'))
weight = float(input('Введите вес в килограммах:'))
IMT = (weight / ((height/100) ** 2))
if IMT < 16:
    print('Выраженный дефицит')
elif 16 <= IMT < 18.49:
    print('Недостаточная')
elif 18.5 <= IMT < 24.99:
    print('Норма')
elif 25 <= IMT < 29.99:
    print('Избыточная')
elif 30 <= IMT < 34.99:
    print('Ожирение 1')
elif 35 <= IMT < 39.99:
    print('Ожирение 2')
else:
    print('Ожирение 3')
