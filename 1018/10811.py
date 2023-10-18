M, N = map(int, input().split())
bascket = [i for i in range(M+1)]

for _ in range(N):
    s, e = map(int, input().split())
    mid = round((e-s+1)/2)
    for i, ind in enumerate(range(s, e+1)):
        if i < mid:
            bascket[ind], bascket[e-i] = bascket[e-i], bascket[ind]

print(*bascket[1:])
