N = int(input())
for _ in range(N):
    a, b = map(str, input().split())
    res = [letter*int(a) for letter in list(b)]
    print(*res, sep="")
