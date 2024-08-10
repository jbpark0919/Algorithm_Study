import sys
input = sys.stdin.readline

N, S = map(int, input().split())
num_list = list(map(int, input().split()))

result = 0

def dfs(i, current_sum):
    global result
    
    if i >= N:
        return
    
    current_sum += num_list[i]
    
    if current_sum == S:
        result += 1
    
    dfs(i + 1, current_sum)
    dfs(i + 1, current_sum - num_list[i])

dfs(0, 0)
print(result)
