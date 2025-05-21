import sys

input = sys.stdin.readline

n, m = map(int, input().split(" "))

바구니 = [0] * n
for element in range(m):
    시작, 끝, 공번호 = list(map(int, input().strip().split(" ")))

    바구니[시작 - 1 : 끝] = [공번호] * (끝 - 시작 + 1)

print(" ".join(map(str, 바구니)))
