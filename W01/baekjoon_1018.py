import sys
input = sys.stdin.readline
N, M = map(int, input().split())

board = []

for i in range(N):
    line = input().strip()
    board.append(list(line))

result = 2500
for row in range(N- 7):
    for col in range(M - 7):
            # 2개의 체스판 순회
            for k in range(2):
                sub_sum_W = 0
                sub_sum_B = 0
                for i in range(row, row+8):
                    for j in range(col, col+8):
                        if (i + j) % 2 == 0:
                            if board[i][j] != 'W':
                                sub_sum_W += 1
                            elif board[i][j] != 'B':
                                sub_sum_B += 1
                        else:
                            if board[i][j] != 'B':
                                sub_sum_W += 1
                            elif board[i][j] != 'W':
                                sub_sum_B += 1
                result = min(min(sub_sum_W, sub_sum_B), result)

print(result)
