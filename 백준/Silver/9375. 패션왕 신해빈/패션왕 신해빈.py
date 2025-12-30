import sys
from io import StringIO


input = sys.stdin.readline

T = int(input())
for i in range(T):
    n = int(input())
    dict = {}
    for j in range(n):
        name, category = input().strip().split(" ")
        if category in dict.keys():
            dict[category].append(name)
        else:
            dict[category] = [name]
    answer = 1
    for names in dict.values():
        answer *= len(names) + 1
    print(answer - 1)
