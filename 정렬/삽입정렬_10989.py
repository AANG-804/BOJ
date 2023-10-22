# 삽입정렬
import sys
k = int(input())
N = [int(i) for i in sys.stdin.read().splitlines()]


for i in range(1, k):
    for j in range(i):
        if N[i-j] < N[i-j-1]:
            N[i-j], N[i-j-1] = N[i-j-1], N[i-j]


print(*N, sep="\n")
