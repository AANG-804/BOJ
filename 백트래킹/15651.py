N, M = map(int, input().split())


def NM(now):
    global N, M, answer
    # 종료조건 - 길이가 M보다 길 때
    if len(now) > M-1:
        answer.append(now)
        return

    for i in range(N):
        NM(now+[i+1])


answer = []
NM([])
for ans in answer:
    print(*ans)
