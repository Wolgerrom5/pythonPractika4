height=float(input('Введите рост в сантиметрах:'))
weight=float(input('Введите вес в килограммах:'))
IMT=(weight/(height**2))
if int(IMT)<16:
    print('Выраженный дефицит')
if 16<=int(IMT)<18.49:
    print('Недостаточная')
if 18.5<=int(IMT)<24.99:
    print('Норма')
if 25<=int(IMT)<29.99:
    print('Избыточная')
if 30<=int(IMT)<34.99:
    print('Ожирение 1')
if 35<=int(IMT)<39.99:
    print('Ожирение 2')
if int(IMT)>=40:
    print('Ожирение 3')