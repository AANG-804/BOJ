import sys
sys.setrecursionlimit(10**6)

N = int(input())


def DFS(left, cnt):
    global memo
    if left == 0:
        return cnt
    if left in memo:
        return memo[left]
    if left < 3:
        return float('inf')

    cnt3 = DFS(left-3, cnt+1)
    cnt5 = DFS(left-5, cnt+1)

    memo[left] = min(cnt3, cnt5)
    return memo[left]


memo = {}
result = DFS(N, 0)
ans = -1 if result == float('inf') else result
print(ans)


# N = int(input())

# # 메모이제이션을 위한 딕셔너리 생성
# memo = {}


# def DFS(left, cnt):
#     # 종료 조건: 남은 left가 0일 때
#     if left == 0:
#         return cnt
#     # 종료 조건: 남은 left가 2보다 작을 때 (더 이상 나눌 수 없을 때)
#     if left < 3:
#         return float('inf')

#     # 메모이제이션 체크
#     if left in memo:
#         return memo[left]

#     # 3과 5로 나누기
#     cnt3 = DFS(left-3, cnt+1)
#     cnt5 = DFS(left-5, cnt+1)

#     # 결과 저장 후 반환
#     memo[left] = min(cnt3, cnt5)
#     return memo[left]


# result = DFS(N, 0)

# # 불가능한 경우 체크
# ans = -1 if result == float('inf') else result
# print(ans)
