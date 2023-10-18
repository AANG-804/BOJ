string = list(input())
reverse = string[::-1]

pel = 1
for a, b in zip(string, reverse):
    if a == b:
        continue
    pel = 0

print(pel)


# alp =list(str(input()))

# if list(reversed(alp)) == alp:
#     print(1)
# else:
#     print(0)
