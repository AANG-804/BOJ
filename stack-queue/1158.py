# N, K = map(int, input().split())

# stack = [i+1 for i in range(N)]
# res = []
# for _ in range(N):
#     for _ in range(K-1 % len(stack)):
#         stack.append(stack.pop(0))
#     res.append(str(stack.pop(0)))

# print("<", ', '.join(res), ">", sep="")

# deque 사용


# 수학 풀이
N, K = map(int, input().split())

stack = [i+1 for i in range(N)]
res = []
num = 0
for _ in range(N):
    num += K-1
    if num > len(stack):
        num %= len(stack)
    res.append(str(stack.pop(num)))

print("<", ', '.join(res), ">", sep="")
