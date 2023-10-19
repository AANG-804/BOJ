
# a, b = input().split()
# a, b = list(a), int(b)

# l = len(a)
# res = 0
# for i, j in enumerate(a):
#     if ord(j) < 58:
#         res += (ord(j) - 48)*(b ** (l-i-1))
#     else:
#         res += (ord(j) - 55)*(b ** (l-i-1))

# print(res)


n, b = input().split()
print(int(n, int(b)))
