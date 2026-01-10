import sys
from io import StringIO

input = sys.stdin.readline


N, P, Q = map(int, input().split())
딸기개수 = list(map(int, input().split()))
샤머개수 = list(map(int, input().split()))

answer = []
possible = True
for i in range(N):
    count = 0

    while 딸기개수[i] != 샤머개수[i]:
        if count == 10000:
            possible = False
            break

        딸기개수[i] = 딸기개수[i] + P
        샤머개수[i] = 샤머개수[i] + Q
        count += 1
    if not possible:
        break
    answer.append(count)
if count == 10000:
    print("NO")
else:
    print("YES")
    print(*answer)
