import sys


input = sys.stdin.readline

n = int(input())

for i in range(1, n):
    print(i * "*" + (2 * (n - i)) * " " + i * "*")

print((2 * (n - 1) + 2) * "*")  # 여기 수정됨

for i in range(n - 1, 0, -1):
    print(i * "*" + (2 * (n - i)) * " " + i * "*")
