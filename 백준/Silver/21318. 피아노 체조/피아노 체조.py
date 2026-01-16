import sys
input = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))
Q = int(input())

if N == 1:
    for _ in range(Q):
        input()
        print(0)
    sys.exit(0)

mistakes = [0] * (N - 1)
for i in range(N - 1):
    mistakes[i] = 1 if a[i] > a[i + 1] else 0

psum = [0] * (N - 1)
psum[0] = mistakes[0]
for i in range(1, N - 1):
    psum[i] = psum[i - 1] + mistakes[i]

for _ in range(Q):
    x, y = map(int, input().split())
    if x == y:
        print(0)
        continue
    l = x - 1
    r = y - 2
    if l == 0:
        print(psum[r])
    else:
        print(psum[r] - psum[l - 1])