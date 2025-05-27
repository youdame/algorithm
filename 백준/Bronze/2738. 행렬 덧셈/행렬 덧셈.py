import sys

input = sys.stdin.readline


n, m = list(map(int, input().split(" ")))

first = []
for i in range(n):
    first.append(list(map(int, input().strip().split(" "))))
# print(first)

second = []
for i in range(n):
    second.append(list(map(int, input().strip().split(" "))))
# print(second)

answer = [[0] * m for i in range(n)]


for i in range(n):
    for j in range(m):
        answer[i][j] = first[i][j] + second[i][j]

for element in answer:
    print(*element)
