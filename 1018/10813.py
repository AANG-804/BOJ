N, M = map(int, input().split())
bascket = [i+1 for i in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    temp = bascket[a-1]
    bascket[a-1] = bascket[b-1]
    bascket[b-1] = temp

print(*bascket)
