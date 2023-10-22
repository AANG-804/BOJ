N, k = map(int, input().split())
scores = [int(i) for i in input().split()]

for i in range(k):
    for j in range(N-i-1):
        if scores[j] > scores[j+1]:
            scores[j], scores[j+1] = scores[j+1], scores[j]

print(scores[-k])
