import sys
from io import StringIO


input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))



# S의 값을 가장 작게 만들기 위해서 수를 배ㅕㅇㄹ하자.. 가장 큰 수랑 가장 작은 수랑 곱해지면 되나?
"""
작은 수랑 작은 수랑 만난다? 

A는 가장 큰 순ㄴ으로 나열
B는 반대로 나열
"""


A.sort()
B.sort(reverse = True)

answer = 0
for i in range(N) :
    answer +=A[i] * B[i]
print(answer)