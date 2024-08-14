N, M = map(int, input().split())

result = 0
graph = {}

def dfs(S, graph, visited):
    
    to_visit = []
        
    to_visit.append(S)
        
    while to_visit:

        node = to_visit.pop()
        
        if node not in visited:
            visited.append(node)
            to_visit.extend(reversed(graph[node]))
        
    return visited

for i in range(1, N+1):
    graph[i] = []

for _ in range(M):
    
    u, v = map(int, input().split())
    
    graph[u].append(v)
    graph[v].append(u)

visited = []

for i in range(1, N+1):
    if i not in visited:
        visited = dfs(i, graph, visited)
        result += 1

print(result)
