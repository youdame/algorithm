import sys
from io import StringIO



input = sys.stdin.readline

arr = [0, 1]

N = int(input())
for i in range(2, N+1):
    arr.append(arr[i-1] * i)


count = 0
for index in range(len(str(arr[N]))-1, 0, -1):

    if str(arr[N])[index] != "0":
        break
    else: 
        count += 1 

print(count)