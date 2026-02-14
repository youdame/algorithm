import sys 
from io import StringIO



input = sys.stdin.readline

num_arr = []
for _ in range(5):
    num_arr.append(list(input().strip()))

arr = [[-1] * 15 for i in range(5)] 
for i in range(5):
    for j in range(15):
        if j < len(num_arr[i]):
            arr[i][j] = num_arr[i][j]

for j in range(15):
    for i in range(5):
        if arr[i][j] != -1:
            print(arr[i][j], end = "")
        