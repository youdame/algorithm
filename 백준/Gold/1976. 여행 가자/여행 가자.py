import sys
from io import StringIO
from collections import deque


input = sys.stdin.readline


N = int(input())
adj = [[] for i in range(N + 1)]
M = int(input())
for i in range(N):
    요소들 = list(map(int, input().strip().split()))
    for j in range(N):
        if 요소들[j] == 1:
            if j + 1 not in adj[i + 1]:
                adj[i + 1].append(j + 1)
            if i + 1 not in adj[j + 1]:
                adj[j + 1].append(i + 1)
route = list(map(int, input().strip().split()))



visited = [False] * (N + 1)

시작 = route[0]

queue = deque([])
queue.append(시작)
visited[시작] = True

while queue:
    pop_node = queue.popleft()
    for new_node in adj[pop_node]:
        # print(new_node)
        if not visited[new_node]:
            visited[new_node] = True
            queue.append(new_node)


flag = True

for node in route:
    if not visited[node]:
        flag = False
        break

print("YES" if flag else "NO")
