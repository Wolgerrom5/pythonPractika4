num = int(input())
if num % 100//10 == 1:
    print(num, "попугаев")
elif num % 10 == 1:
    print(num, "попугай")
elif num % 10 in [2, 3, 4]:
    print(num, "попугая")
else:
    print(num, "попугаев")