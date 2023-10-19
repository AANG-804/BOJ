A = []
for i in range(100):
    A.append([""]*100)

for _ in range(int(input())):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            A[x+i][y+j] = "*"


num = [row.count("*") for row in A]
print(sum(num))
