import sys
from io import StringIO



input = sys.stdin.readline

n = int(input())
m = int(input())

adj = [[] for i in range(n + 1)]

visited = [False] * (n + 1)

for i in range(m):
    a, b = list(map(int, input().split(" ")))
    adj[a].append(b)
    adj[b].append(a)

visited[1] = True
answer = 0

for 친구들 in adj[1]:
    if not visited[친구들]:
        visited[친구들] = True
        answer += 1
    for 친구의친구 in adj[친구들]:
        if not visited[친구의친구]:
            visited[친구의친구] = True
            answer += 1
print(answer)
