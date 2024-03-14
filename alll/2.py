import math
xc, yc = map(float, input().split())  # координаты центра окружности
r = float(input())
xp, yp = map(float, input().split())  # координаты точки
distance = math.sqrt((xp - xc)**2 + (yp - yc)**2)
if distance < r:
    print("Точка находится внутри окружности")
elif distance == r:
    print("Точка лежит на окружности")
else:
    print("Точка находится за пределами окружности")