import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())

num_list = list(map(int, input().split()))

sort_num_list = sorted(set(num_list))

# index(): O(N), bisect(): O(logN)
for i in range(len(num_list)):
    print(bisect_left(sort_num_list, num_list[i]), end=' ')
