import sys

input = sys.stdin.readline


배열리스트 = []
for _ in range(9):
    배열리스트.append(list(map(int, input().strip().split())))

좌표 = [0, 0]
max_val = -1

for i in range(9):
    for j in range(9):
        if 배열리스트[i][j] > max_val:
            max_val = 배열리스트[i][j]
            좌표 = [i + 1, j + 1]  # 문제는 1-indexed 좌표를 요구함

print(max_val)
print(좌표[0], 좌표[1])
