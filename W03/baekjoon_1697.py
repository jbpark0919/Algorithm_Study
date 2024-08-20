from collections import deque

N, K = map(int, input().split())

dist = [0] * 200001

def func(z, current):
    if z == 0:
        return current-1
    elif z == 1:
        return current+1
    else:
        return 2*current

def bfs(s):
    to_visited = deque()
    to_visited.append(s)
    
    while to_visited:
        node = to_visited.popleft()
        
        for z in range(3):
            next_node = func(z, node)
            
            if 0 <= next_node <= 200000 and dist[next_node] == 0:
                to_visited.append(next_node)
                dist[next_node] = dist[node] + 1
                
                if next_node == K:
                    return

bfs(N)

if N == K:
    print(0)
else:
    print(dist[K])
