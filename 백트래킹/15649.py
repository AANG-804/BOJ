
def NM(now):
    global answer, M, N
    # M개 뽑으면 스탑
    if len(now) > M-1:
        answer.append(now)
        return

    for i in range(N):
        if i+1 in now:
            continue
        NM(now+[i+1])


N, M = map(int, input().split())
answer = []
NM([])

for ans in answer:
    print(*ans)
