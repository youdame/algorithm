import sys
from io import StringIO


input = sys.stdin.readline

현재사람수 = 0
max_사람수 = 0
for i in range(10):
    내린사람수, 탄사람수 = list(map(int, input().split()))
    현재사람수 -= 내린사람수
    현재사람수 += 탄사람수
    max_사람수 = max(max_사람수, 현재사람수)
print(max_사람수)
