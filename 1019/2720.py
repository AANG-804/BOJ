N = int(input())
t = [25, 10, 5]

for i in range(N):
    res = []
    a = int(input())
    for i in t:
        print(a // i, end=" ")
        a = a % i
    print(a)
