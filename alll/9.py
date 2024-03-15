heights = list(map(int, input().split()))
n = len(heights)
for i in range(n):
    for j in range(n - 1):
        if heights[j] < heights[j + 1]:
            heights[j], heights[j + 1] = heights[j + 1], heights[j]
print(heights)
