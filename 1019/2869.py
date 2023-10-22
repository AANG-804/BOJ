A, B, V = map(int, input().split())

a = (V - A)//(A - B)
b = (V - A) % (A - B)
if b == 0:
    print(a+1)
else:
    print(a+2)
