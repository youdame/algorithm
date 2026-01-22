import sys
input = sys.stdin.readline

N, L, D = map(int, input().split())

block = L + 5
end_time = N * block - 5

k = 0
while True:
    t = k * D

    if t >= end_time:
        print(t)
        break

    if t % block >= L:
        print(t)
        break

    k += 1