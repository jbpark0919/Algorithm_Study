t = int(input())

DP = [0]*12
DP[1] = 1
DP[2] = 2
DP[3] = 4

for i in range(4, 12):
    DP[i] = DP[i-1] + DP[i-2] + DP[i-3]

for _ in range(t):
    n = int(input())
    
    print(DP[n])
