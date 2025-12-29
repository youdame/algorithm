import sys
from io import StringIO
import heapq


input = sys.stdin.readline
N = int(input())

pq = []  # 힙
숫자들 = [int(input()) for i in range(N)]
count = 숫자들.count(0)
# print(count)
i = 0
for i in range(N):
    숫자 = 숫자들[i]
    # print(pq)
    if 숫자 != 0:
        heapq.heappush(pq, -1 * 숫자)
    else:
        # count -= 1
        if pq:
            print(abs(heapq.heappop(pq)))
        else:
            print(0)
