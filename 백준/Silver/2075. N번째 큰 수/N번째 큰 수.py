import sys
from io import StringIO
import heapq

input = sys.stdin.readline


N = int(input())

heap = []

for i in range(N):
    for element in list(map(int, input().split())):
        if len(heap) == N:
            if heap[0] < element:
                heapq.heappop(heap)
                heapq.heappush(heap, element)
        else:
            heapq.heappush(heap, element)
print(heap[0])
