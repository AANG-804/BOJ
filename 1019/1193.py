N = int(input())

i = 1
j = 1
while (N > (i**2+i)/2):
    i += 1
    j = int((i**2+i)/2)

p = j-N
if i % 2 == 0:
    print(f'{i-p}/{1+p}')
else:
    print(f'{1+p}/{i-p}')
