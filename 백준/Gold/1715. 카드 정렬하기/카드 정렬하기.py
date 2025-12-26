import sys
from io import StringIO
from queue import PriorityQueue



input = sys.stdin.readline

N = int(input())
pq = PriorityQueue()
for i in range(N):
    pq.put(int(input()))

answer = 0

while pq.qsize() > 1:
    하나 = pq.get()
    둘 = pq.get()
    answer += 하나 + 둘
    pq.put(하나 + 둘)

print(answer)
