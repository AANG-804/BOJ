# ord('A') = 65
a = [ord(i)-65 for i in list(input())]
dial = {2: [0, 1, 2], 3: [3, 4, 5], 4: [6, 7, 8], 5: [9, 10, 11], 6: [
    12, 13, 14], 7: [15, 16, 17, 18], 8: [19, 20, 21], 9: [22, 23, 24, 25]}
res = 0
for inp in a:
    for key, value in dial.items():
        if inp in value:
            res += key+1

print(res)

# a=0
# l='33344455566677788889990000'
# for i in input():
#     i=int(l[ord(i)-ord('A')])
#     if i:a+=i
#     else:a+=10
# print(a)
