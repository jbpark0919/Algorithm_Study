import sys
input = sys.stdin.readline

L, C = map(int, input().split())
char_list = list(input().split())
char_list.sort()

def dfs(index, result, mo, ja):
    
    if len(result) == L:
        if mo >= 1 and ja >= 2:
            print(result)
        return
    
    for i in range(index, C):
        if char_list[i] in 'aeiou':
            dfs(i + 1, result + char_list[i], mo + 1, ja)
        else:
            dfs(i + 1, result + char_list[i], mo, ja + 1)
        
dfs(0, '', 0, 0)
