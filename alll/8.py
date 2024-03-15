n = int(input("Введите количество кнатов: "))
galleon = n // (17*29)
sickle = (n % (17 *29)) // 29
knut = n % 29
if galleon:
    print(f"{galleon} галлеонов")
if sickle:
    print(f"{sickle} сиклей")
if knut:
    print(f"{knut} кнатов")