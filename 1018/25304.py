total = int(input())
rep = int(input())
total_ = 0
for _ in range(rep):
    a, b = map(int, input().split())
    total_ += a*b

if total == total_:
    print("Yes")
else:
    print("No")
