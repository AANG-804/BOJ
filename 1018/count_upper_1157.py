s = [ord(a) for a in list(input())]
d = {}

for i in s:
    if i > 90:
        i -= 32
    if d.get(i) == None:
        d[i] = 1
    else:
        d[i] += 1

max_a = max(list(d.values()))
alp = chr(list(d.keys())[list(d.values()).index(max_a)])

cnt = 0
for i in d.values():
    if i == max_a:
        cnt += 1
    if cnt > 1:
        alp = "?"
        break

print(alp)


# import sys
# x = sys.stdin.read()
# x=x.upper()
# arr = [0 for _ in range(91-65)]
# for i in range(65,91):
#     c=chr(i)
#     count=x.count(c)
#     arr[i-65]=count

# M = max(arr)
# if arr.count(M) > 1:
#     print('?')
# else:
#     print(chr(arr.index(M)+65))
