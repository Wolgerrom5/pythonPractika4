num = int(input())
if num == int(str(num)[::-1]):
    print("настоящее")
else:
    print("кривое")