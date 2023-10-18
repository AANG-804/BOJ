def is_group(word):
    word_set = set(word)

    for a in word_set:
        temp = word
        for b in word_set-set(a):
            temp = temp.replace(b, " ")
        cnt = len(temp.split())
        if cnt > 1:
            return 0
    return 1


N = int(input())

res = 0
for _ in range(N):
    word = input()
    res += is_group(word)

print(res)
