
from copy import deepcopy


def DFS(fr):
    global graph, visited
    visited[fr] = True
    print(fr, end=" ")

    # 1. 기본동작
    for i in range(1, N+1):
        if not visited[i] and graph[fr][i]:
            graph[i][fr] = False
            DFS(i)


def bfs():
    global q, graph_BFS, visited
    while q:
        cur = q.pop(0)
        print(cur, end=' ')
        for i in range(1, N+1):
            if not visited[i] and graph_BFS[cur][i]:
                visited[i] = True
                q.append(i)


N, M, V = map(int, input().split())

graph = [[False]*(N+1) for i in range(N+1)]
visited = [False]*(N+1)
for i in range(M):
    fr, to = map(int, input().split())
    graph[fr][to], graph[to][fr] = True, True
graph_BFS = deepcopy(graph)

DFS(V)
print()

visited = [False]*(N+1)
q = [V]
visited[V] = True
bfs()
