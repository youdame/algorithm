import sys


input = sys.stdin.readline

n, m = map(int, input().split(" "))

바구니 = [i for i in range(1, n + 1)]

for element in range(m):
    시작, 끝 = list(map(int, input().strip().split(" ")))
    바구니[시작 - 1 : 끝] = 바구니[시작 - 1 : 끝][::-1]

print(" ".join(map(str, 바구니)))
