N = int(input())

i = 0
j = 665
while (N > i):
    if str(j).find('666') != -1:
        i += 1
        j += 1
    else:
        j += 1
print(j-1)
