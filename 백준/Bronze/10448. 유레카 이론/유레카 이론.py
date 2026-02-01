import sys
from io import StringIO
from itertools import combinations_with_replacement


input = sys.stdin.readline
# 3개로 표현된다는 것의 의미가 무엇일까? K는 1000보다 작다

T = int(input())

arr = []
for i in range(1, 45):
    arr.append(i * (i+1) // 2)

for _ in range(T):
    K = int(input())
    for comb in combinations_with_replacement(arr, 3):
        if sum(comb) == K:
            print(1)
            break
    else: 
        print(0)

    