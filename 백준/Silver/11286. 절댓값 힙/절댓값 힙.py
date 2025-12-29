import sys
from io import StringIO
import heapq


input = sys.stdin.readline
N = int(input())

pq = []  # 힙
숫자들 = [int(input()) for i in range(N)]
count = 숫자들.count(0)
# print(count)
for i in range(N):

    숫자 = 숫자들[i]
    # print(pq)
    if 숫자 != 0:
        heapq.heappush(pq, (abs(숫자), -1 if 숫자 < 0 else 1))
    else:
        # count -= 1
        if pq:
            뽑은값 = heapq.heappop(pq)
            print(-1 * 뽑은값[0] if 뽑은값[1] < 0 else 뽑은값[0])
        else:
            print(0)
    # print(pq)
