import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

psum = [0] * n
psum[0] = arr[0]
for i in range(1, n):
    psum[i] = psum[i-1] + arr[i]

total = psum[-1]
ans = 0

# case 1: 벌(0), 벌(i), 벌통(n-1)
# 총 = 2*sum(i+1..n-1) + sum(1..i-1)   (단, 시작칸 0, i는 어떤 벌도 못 캠)
for i in range(1, n-1):
    two = 2 * (total - psum[i])                 # i+1..n-1을 두 번
    one = (psum[i-1] - arr[0])                  # 1..i-1을 한 번
    ans = max(ans, two + one)

# case 2: 벌통(0), 벌(i), 벌(n-1)  (case1 대칭)
# 총 = 2*sum(0..i-1) + sum(i+1..n-2)
for i in range(1, n-1):
    two = 2 * psum[i-1]                         # 0..i-1을 두 번 (0은 벌통)
    one = (psum[n-2] - psum[i])                 # i+1..n-2를 한 번
    ans = max(ans, two + one)

# case 3: 벌(0), 벌통(i), 벌(n-1)
# 합(1..n-2)은 한 번 + 벌통 i는 한 번 더 (두 번 먹히니까)
base = psum[n-2] - arr[0]                       # 1..n-2 한 번 (0은 시작이라 못 캠)
for i in range(1, n-1):
    ans = max(ans, base + arr[i])

print(ans)