a, b = map(list, input().split())
a, b = int("".join(reversed(a))), int("".join(reversed(b)))
print(max(a, b))


# 술라이싱 [::-1]
