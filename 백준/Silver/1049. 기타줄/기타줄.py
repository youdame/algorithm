import sys
from io import StringIO
import math

input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
for _ in range(M):
    package_price, item_price = map(int, input().split())
    arr.append((package_price, item_price))

min_package = min(arr, key=lambda x: x[0])[0]
min_item = min(arr, key=lambda x: x[1])[1]

# 전부 패키지로 사는 경우 
case1 = min_package * ((N // 6) + 1) 

# 일부만 패키지로 사는 경우 
case2 = min_package * (N // 6) + min_item * (N % 6)

# 전부 낱개로 사는 경우 
case3 = min_item * N

print(min(case1, case2, case3))