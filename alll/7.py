N, K, M = map(int, input().split())
if M > K:
    distance = M - K - 1
    distance_1 = N - M + K - 1
    min_distance = min(distance, distance_1)
else:
    distance = M + (N - K) - 1
    distance_1 = K - M - 1
    min_distance = min(distance, distance_1)
print(min_distance)
