from collections import deque

N, K = map(int, input().split())

stack = deque([i+1 for i in range(N)])
res = []
for _ in range(N):
    stack.rotate(-(K-1 % len(stack)))
    res.append(str(stack.popleft()))

print("<", ', '.join(res), ">", sep="")


# 수학 풀이
# N, K = map(int, input().split())

# stack = [i+1 for i in range(N)]
# res = []
# num = 0
# for _ in range(N):
#     num += K-1
#     if num > len(stack):
#         num %= len(stack)
#     res.append(str(stack.pop(num)))

# print("<", ', '.join(res), ">", sep="")
