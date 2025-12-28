import sys
from io import StringIO
from collections import deque

input = sys.stdin.readline

n, m = list(map(int, input().split()))

adj = [[] for i in range(n + 1)]
for i in range(m):
    A, B = list(map(int, input().split()))
    adj[A].append(B)

answer = []
수강해야하는과목수 = [0] * (n + 1)
for index in range(1, len(adj)):
    for element in adj[index]:
        수강해야하는과목수[element] += 1


선수과목없음 = deque()
for i in range(1, n + 1):
    if 수강해야하는과목수[i] == 0:
        선수과목없음.append(i)

while 선수과목없음:
    # print(선수과목없음)
    선수과목없는노드 = 선수과목없음.popleft()
    answer.append(선수과목없는노드)

    for 인접노드 in adj[선수과목없는노드]:

        if 수강해야하는과목수[인접노드] >= 0:
            수강해야하는과목수[인접노드] -= 1
        if 수강해야하는과목수[인접노드] == 0:
            선수과목없음.append(인접노드)


전체노드 = [i for i in range(1, n + 1)]

print(*answer)
