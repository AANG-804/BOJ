from collections import deque


def printer(queue, N, M):
    queue = deque(queue)
    idx = deque(range(N))
    ans = 0
    while True:
        # 프린트하려고 보니 뒤에 중요한게 있음 -> 건방진 녀석 맨 뒤로 가
        if queue.index(max(queue)) != 0:
            queue.rotate(-1)
            idx.rotate(-1)
        else:
            # 루프 탈출 조건 - 이제 프린트하려는게 딱! 궁금한 그 녀석일 때
            if idx[0] == M:
                return ans+1
            queue.popleft()
            idx.popleft()
            ans += 1


K = int(input())

for _ in range(K):
    N, M = map(int, input().split())
    queue = [int(i) for i in input().split()]
    print(printer(queue, N, M))
