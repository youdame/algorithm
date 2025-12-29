import sys
from io import StringIO
from collections import deque



input = sys.stdin.readline

T = int(input())

for i in range(T):
    N, M = list(map(int, input().split()))
    중요도 = deque()
    문서들 = list(map(int, input().split()))
    for i in range(len(문서들)):
        중요도.append((문서들[i], i))
    i = 0
    while 중요도:
        if 중요도[0][0] != max(중요도)[0]:
            중요도.append(중요도.popleft())
        else:
            뽑히는값 = 중요도.popleft()
            i += 1
            if 뽑히는값[1] == M:
                print(i)
