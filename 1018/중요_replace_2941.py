alp = list(input())


def search(string: list, target: list):
    m = len(target)
    cnt = 0
    i = 0
    while (i+m <= len(string)):
        if string[i:i+m] == target:
            string[i:i+m] = [0]*m
            cnt += 1
        i += 1
    return string, cnt, m


targets = ["c=", "c-", 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

remaining = len(alp)
res = 0
for target in targets:
    alp, cnt, m = search(alp, list(target))
    # print(alp, target, cnt, m)
    res += cnt
    remaining -= m*cnt

print(res + remaining)

# word = input()
# lst = ['c=','c-','dz=','d-','lj','nj','s=','z=']
# for i in lst:
#     word = word.replace(i,'*')
# print(len(word))
