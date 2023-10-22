
# def NM(now):
#     global answer, M, N
#     # M개 뽑으면 스탑
#     if len(now) > M-1:
#         answer.append("".join([str(a) for a in sorted(now)]))
#         return

#     for i in range(N):
#         if i+1 in now:
#             continue
#         NM(now+[i+1])


# N, M = map(int, input().split())
# answer = []
# NM([])
# answer = sorted(list(set(answer)))
# for ans in answer:
#     print(*ans)


import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())


def backtrack(i, N, M, lst):

    # 종료조건 1
    if len(lst) == M:
        print(*lst)
        return

    # 종료조건 2
    if i == N + 1:
        return

    # 재귀 호출
    backtrack(i + 1, N, M, lst + [i])
    backtrack(i + 1, N, M, lst)


backtrack(1, N, M, [])
