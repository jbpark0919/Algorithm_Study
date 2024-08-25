n = int(input())
num_list = list(map(int, input().split()))

dp = [0]*n
dp[0] = num_list[0]
answer = dp[0]

for i in range(1, len(num_list)):
    dp[i] = max(dp[i-1] + num_list[i], num_list[i])
    answer = max(answer, dp[i])

print(answer)
