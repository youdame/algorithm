import sys
from io import StringIO
from itertools import combinations

input = sys.stdin.readline


난쟁이들 = [int(input()) for _ in range(9)]
answer = []
for 난쟁이후보 in combinations(난쟁이들, 7):
    if sum(난쟁이후보) == 100:
        answer = 난쟁이후보
        break
for 난쟁이 in answer:
    print(난쟁이)
