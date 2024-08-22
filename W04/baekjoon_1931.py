n = int(input())

times = []

for i in range(n):
    s, e = map(int, input().split())
    
    times.append([s, e])

times.sort(key = lambda x: (x[1], x[0]))

end = 0
answer = 0

for s, e in times:
    if s >= end:
        answer += 1
        end = e

# print(times)
print(answer)
