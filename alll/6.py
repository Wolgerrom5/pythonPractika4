day1 = int(input())
day2 = int(input())
day3 = int(input())
counts = [day1, day2, day3]
repetitions = 0
for i in range(len(counts)):
    if counts.count(counts[i]) > 1:  # Если количество встречается более одного раза
        repetitions += 1
print(repetitions)

