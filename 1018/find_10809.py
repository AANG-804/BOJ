alp = list("abcdefghijklmnopqrstuvwxyz")
res = [-1]*len(alp)
text = input()
for _, a in enumerate(alp):
    try:
        res[_] = text.index(a)
    except:
        pass

print(*res)

# .find() 함수 사용하기
