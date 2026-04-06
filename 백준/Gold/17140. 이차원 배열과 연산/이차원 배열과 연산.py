
import sys 

from io import StringIO
from collections import defaultdict



input = sys.stdin.readline

r, c, k = map(int, input().split())

arr = []

for _ in range(3):
    arr.append(list(map(int, input().split())))


def make_new_arr(arr , method):    
    if method == "C":
        arr = list(map(list, zip(*arr)))

    n = len(arr)
    m = len(arr[0])
    
    max_length = 0
    
    new_arr = []
    for j in range(n):
        new_row_dict = defaultdict(int)
        new_row = []
        
        for k in range(m):
            if arr[j][k] != 0:
                new_row_dict[arr[j][k]] += 1
        
        temp_row = list(sorted(new_row_dict.items(),key=lambda x : (x[1], x[0])))

        for num, count in temp_row:
            new_row.extend([num, count])
            new_row = new_row[:100]

        max_length = max(max_length, len(new_row))

        new_arr.append(new_row)
        
    for row in new_arr:
        if len(row) < max_length:
            row.extend([0] * (max_length - len(row)))

        
    if method == "C":
        new_arr = list(map(list, zip(*new_arr)))
    
    return new_arr


i = 0

while i <=100:
        
    if r-1 < len(arr) and c-1 < len(arr[0]):
        if arr[r-1][c-1] == k:
            print(i) 
            sys.exit()  

    n = len(arr)
    m = len(arr[0])
    if n >= m:
        new_arr = make_new_arr(arr, "R")
    else:
        new_arr = make_new_arr(arr, "C")
            
    arr = new_arr

    i += 1
print(-1)










    