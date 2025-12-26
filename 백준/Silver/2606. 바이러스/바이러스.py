import sys
from io import StringIO

input = sys.stdin.readline

컴퓨터수 = int(input())
짝수 = int(input())

adj = [[] for i in range(컴퓨터수 + 1)]
visited = [False] * (컴퓨터수 + 1)
for i in range(짝수):
    a, b = list(map(int, input().split(" ")))
    adj[a].append(b)
    adj[b].append(a)


answer = 0
visited[1] = True


def dfs(node):
    visited[node] = True
    global answer
    for new_node in adj[node]:
        if not visited[new_node]:
            answer += 1

            dfs(new_node)
    return answer


print(dfs(1))
