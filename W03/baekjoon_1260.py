from collections import deque

N, M, S = map(int, input().split())

edges = []
graph = {}
for i in range(1, N + 1):
    graph[i] = []

for i in range(M):
    u, v = map(int, input().split())
    edges.append((u, v))

for node1, node2 in edges:
    graph[node1].append(node2)
    graph[node2].append(node1)

for i in graph:
    graph[i].sort()

def dfs(graph, S):
    to_visit, visited = [], []
    to_visit.append(S)
    
    while to_visit:
        node = to_visit.pop()
        if node not in visited:
            print(node, end=' ')
            visited.append(node)
            to_visit.extend(reversed(graph[node]))

def bfs(graph, S):
    to_visit, visited = deque(), []
    to_visit.append(S)
    
    while to_visit:
        node = to_visit.popleft()
        
        if node not in visited:
            print(node, end=' ')
            visited.append(node)
            to_visit.extend(graph[node])

dfs(graph, S)
print()
bfs(graph, S)
