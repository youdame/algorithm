import sys 
from io import StringIO
from collections import deque


input = sys.stdin.readline

N, K = map(int, input().split())

queue = deque([])


MAX = 100001
distance = [1e9] * MAX
visited = [False] * MAX
wherefrom = [1e9] * MAX
queue.append(N)
distance[N] = 0
visited[N] = True



while queue:
    node = queue.popleft()
    for next in (node + 1, node - 1, node * 2):
        if 0 <= next <= 100000 and not visited[next]:
            visited[next] = True
            queue.append(next)
            distance[next] = min(distance[next], distance[node] + 1)
            wherefrom[next] = node

    
print(distance[K])

answer = [K]
current = K

while current != N:
    current = wherefrom[current]
    answer.append(current)

print(*answer[::-1])