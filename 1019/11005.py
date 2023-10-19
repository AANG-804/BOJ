a, b = map(int, input().split())

res = []

while (a > 0):
    res.append(a % b)
    a = a//b

for i in res[::-1]:
    if i < 10:
        print(i, end='')
    else:
        print(chr(i+55), end='')
