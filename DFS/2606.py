import sys
from copy import deepcopy


def DFS(start, data):
    global computers
    # 1. 시작점에서 이어진 브랜치 찾기
    data_temp = deepcopy(data)
    branchs = [branch for branch in data_temp if start in branch]
    for branch in branchs:
        data_temp.remove(branch)
    # 2. 감염된 컴퓨터 저장
    computers[start] = 1
    # 정지 조건 1 - 시작점과 이어진 브랜치가 더이상 없는 경우
    if len(branchs) == 0:
        return
    # 2. 브랜치에 이어진 곳으로 재귀호출
    for branch in branchs:
        print(branch[int(not branch.index(start))])
        DFS(branch[int(not branch.index(start))], data_temp)


lines = sys.stdin.read().splitlines()
N, M = int(lines[0]), lines[1]
data = [[int(line[0]), int(line[2])] for line in lines[2:]]
computers = [0]*(N+1)

DFS(N, data)
print(sum(computers))
