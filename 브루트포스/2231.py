N = int(input())

for i in range(N):
    tmp = i
    j = i
    while (tmp > 0):
        j += tmp % 10
        tmp = tmp//10
    if (j == N):
        print(i)
        break

if (i == N-1):
    print(0)
