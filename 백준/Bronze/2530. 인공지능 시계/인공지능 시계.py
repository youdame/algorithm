import sys
from io import StringIO

input = sys.stdin.readline

A, B, C = list(map(int, input().split()))
D = int(input())

C = C + D

초 = C % 60
분 = B + (C // 60)
시간 = A
if 분 >= 60:
    시간 += 분 // 60
    분 = 분 % 60

if 시간 >= 24:
    시간 = 시간 % 24
print(시간, 분, 초)
