import sys 
from io import StringIO


input = sys.stdin.readline

num_arr = []
for _ in range(5):
    num_arr.append(list(input().strip()))

for j in range(15):
    for i in range(5):
        if j < len(num_arr[i]):
            print(num_arr[i][j], end="")