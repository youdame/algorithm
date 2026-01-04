import sys
from io import StringIO
from itertools import combinations

input = sys.stdin.readline

N = int(input())

표본 = [i for i in range(10)]
# print(표본)
answer = []

for i in range(1, 11):
    answer += list(combinations(표본, i))
answer.sort(key=lambda x: (len(x), x[::-1]))
# print(answer)

if N >= len(answer):
    print(-1)
else:
    print("".join(map(str, sorted(answer[N], reverse=True))))
