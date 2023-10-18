N, M = map(int, input().split())

matA = []
for i in range(N):
    matA.append([int(j) for j in input().split()])

matB = []
for i in range(N):
    matB.append([int(j) for j in input().split()])

matC = []
for a in range(N):
    temp = []
    for b in range(M):
        temp.append(matA[a][b] + matB[a][b])
    matC.append(temp)

for row in matC:
    print(*row)
