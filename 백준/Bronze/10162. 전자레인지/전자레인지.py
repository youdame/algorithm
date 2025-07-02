import sys

초 = [300, 60, 10]

count = [0, 0, 0]
input = sys.stdin.readline

인풋 = int(input())

for i in range(len(초)):
    if 인풋 - 초[i] >= 0:
        count[i] = 인풋 // 초[i]
        인풋 %= 초[i]

if 인풋 != 0:
    print(-1)
else:
    print(" ".join(map(str, count)))
