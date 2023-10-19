import sys

lines = sys.stdin.read().splitlines()
mat = []
for line in lines:
    mat.append([int(i) for i in line.split()])

max_num = 0
max_row = 0
for i, row in enumerate(mat):
    m = max(row)
    if max_num < m:
        max_num = m
        max_row = i

print(max_num)
print(max_row+1, mat[max_row].index(max_num) + 1)
