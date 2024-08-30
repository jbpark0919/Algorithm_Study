n = int(input())

DP = [0]*301
step = [0]*301

for i in range(1, n+1):
    step[i] = int(input())

DP[1] = step[1]
DP[2] = step[1] + step[2]
DP[3] = max(step[1] + step[3], step[2] + step[3])

for i in range(4, n+1):
    DP[i] = max(DP[i-2] + step[i], DP[i-3] + step[i-1] + step[i])

print(DP[n])
