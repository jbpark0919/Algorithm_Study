t = int(input())

for _ in range(t):
    n = int(input())
    
    num_list = list(map(int, input().split()))
    
    result = 0
    max_num = 0
    for i in range(len(num_list)-1, -1, -1):
        if num_list[i] > max_num:
            max_num = num_list[i]
        else:
            result += max_num - num_list[i]
    
    print(result)
