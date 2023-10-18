a = [1, 1, 2, 2, 2, 8]
inp = input().split()

for a, b in zip(a, inp):
    print(a-int(b), end=" ")
