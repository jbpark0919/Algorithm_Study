from collections import deque

N, M, K = map(int, input().split())

trash_map = [[0]*M for _ in range(N)]
visited = set()

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for _ in range(K):
    r, c = map(int, input().split())
    trash_map[r-1][c-1] = 1

def bfs(i, j):
    cnt = 1
    to_visited = deque()
    to_visited.append((i, j))
    visited.add((i, j))
    
    while to_visited:
        current_i, current_j = to_visited.popleft()
        
        for z in range(4):
            tmp_i = current_i + dy[z]
            tmp_j = current_j + dx[z]
            
            if tmp_i < 0 or tmp_j < 0 or tmp_i >= N or tmp_j >= M:
                continue
            
            if (tmp_i, tmp_j) not in visited and trash_map[tmp_i][tmp_j] == 1:
                cnt += 1
                visited.add((tmp_i, tmp_j))
                to_visited.append((tmp_i, tmp_j))
    
    return cnt
    
result = 0

for i in range(N):
    for j in range(M):
        if (i, j) not in visited and trash_map[i][j] == 1:
            result = max(result, bfs(i, j))

print(result)
