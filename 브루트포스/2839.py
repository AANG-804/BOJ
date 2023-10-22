N = int(input())
res5, left = N//5, N % 5

res3 = 0
while left >= 3 or res5 > 0:
    res3 += left//3
    left = left % 3
    if res5 > 0 and left > 0:
        left += 5
        res5 -= 1
    elif left == 0:
        print(res3 + res5)
        break
    else:
        print(-1)
        break
