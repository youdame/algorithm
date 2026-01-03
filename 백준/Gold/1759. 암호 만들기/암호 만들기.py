import sys
from io import StringIO
from itertools import combinations

input = sys.stdin.readline
L, C = list(map(int, input().split()))
arr = input().split()
# print(L, C, arr)

모음 = []
자음 = []
for element in arr:
    if element in ("a", "e", "i", "o", "u"):
        모음.append(element)
    else:
        자음.append(element)

조합 = []
for i in range(16):
    for j in range(16):
        if i + j == L and i >= 1 and j >= 2 and i <= len(모음) and j <= len(자음):
            조합.append((i, j))

answer = []
for 모음개수, 자음개수 in 조합:
    for 모음하나 in list(combinations(모음, 모음개수)):
        for 자음하나 in list(combinations(자음, 자음개수)):
            answer.append("".join(list(sorted(자음하나 + 모음하나))))

for element in sorted(answer):
    print(element)
