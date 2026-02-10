import sys 
from io import StringIO
from collections import deque


input = sys.stdin.readline


N, K = map(int, input().split())

queue = deque([])
MAX = 100001

distance = [1e9] * MAX
queue.append(N)
distance[N] = 0

while queue:
    node = queue.popleft()
    for next in (node + 1, node - 1):
        if 0 <= next <= 100000:
            if distance[next] > distance[node] + 1:
                queue.append(next)
                distance[next] = distance[node] + 1

    next = node * 2
    if 0 <= next <= 100000:
        if distance[next] > distance[node]:
            queue.appendleft(next)
            distance[next] = distance[node]


print(distance[K])
