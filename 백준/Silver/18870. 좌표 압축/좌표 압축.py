import sys
from io import StringIO


input = sys.stdin.readline
N = int(input())
초기값 = list(map(int, input().split(" ")))
arr = sorted(초기값)
dict = {}
가장큰값 = -10e9
index = 0
for i in range(N):
    if 가장큰값 < arr[i]:
        index += 1
    가장큰값 = arr[i]
    dict[arr[i]] = index - 1


answer = []
for i in range(N):
    answer.append(dict[초기값[i]])
print(*answer)
