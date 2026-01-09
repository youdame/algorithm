import sys
from io import StringIO


input = sys.stdin.readline


N = int(input())
입력 = input().strip()
answer = 0
for index in range(len(입력)):
    answer = (answer + (ord(입력[index]) - ord("a") + 1) * pow(31, index)) % 1234567891

print(answer)
