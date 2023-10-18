a, b = map(int, input().split())
bascket = [0 for _ in range(a)]

for i in range(b):
    s, e, n = map(int, input().split())
    for ind in list(range(s-1, e)):
        bascket[ind] = n

for _ in bascket:
    print(_, end=" ")
