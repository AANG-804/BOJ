# 버블 정렬
import sys
N = [int(i) for i in sys.stdin.read().splitlines()[1:]]


for i in range(len(N)-1):
    for j in range(len(N)-i-1):
        if N[j] > N[j+1]:
            N[j], N[j+1] = N[j+1], N[j]


print(*N, sep="\n")
