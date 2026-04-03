import sys
from io import StringIO
from collections import defaultdict
input = sys.stdin.readline

"""
뭐라는 거지..
A의 부배열 합 + B의 부배열 합 = T를 만족하는 부 배열의 쌍의 개수 

개수만 구하면 됨..

A에서 몇 개, B에서 몇 개 골라서 T 만들기 
대신 순차적이어야함

"""

T = int(input())

n = int(input())
A = list(map(int, input().split()))

m = int(input())
B = list(map(int, input().split()))

A_record = defaultdict(int)
for i in range(n):
    current = 0
    for j in range(i, n):
        current += A[j]
        A_record[current] += 1

answer = 0

for i in range(m):
    current = 0
    for j in range(i, m):
        current += B[j]

        나머지 = T - current
        if 나머지 in A_record:
            answer += A_record[나머지]
 
print(answer)
