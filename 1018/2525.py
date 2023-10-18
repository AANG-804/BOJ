H_now, M_now = map(int, input().split())
M_add = int(input())

total = H_now*60 + M_now + M_add

H = (total//60) % 24
M = total-(total//60)*60

print(H, M)
