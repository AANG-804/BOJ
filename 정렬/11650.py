# N = int(input())

# dots = []
# for _ in range(N):
#     x, y = map(int, input().split())
#     dots.append((x, y))

# for dot in sorted(dots):
#     print(*dot)

N = int(input())

dots = []
for _ in range(N):
    x, y = map(int, input().split())
    dots.append((y, x))

for dot in sorted(dots):
    print(dot[1], dot[0])
