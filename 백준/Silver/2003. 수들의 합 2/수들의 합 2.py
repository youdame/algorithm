import sys
from io import StringIO



input = sys.stdin.readline

N, M = list(map(int, input().strip().split(" ")))

arr = list(map(int, input().strip().split(" ")))
left = 0
right = 0
count = 0
합 = 0
i = 0
while right < N + 1:
    if 합 == M:
        count += 1
        합 -= arr[left]
        left += 1

    elif 합 > M:
        합 -= arr[left]
        left += 1
    else:
        if right == N:
            break
        합 += arr[right]
        right += 1

print(count)
