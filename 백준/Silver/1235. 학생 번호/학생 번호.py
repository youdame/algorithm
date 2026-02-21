import sys
from io import StringIO


N = int(input())

arr = []
for _ in range(N):
    arr.append(input().strip()[::-1])


answer = 1
set_arr = []

while True:
    
    for i in range(len(arr)):
        set_arr.append(arr[i][0:answer])
    if len(set(set_arr)) == N:
        break
    else:
        answer += 1
        set_arr = []
print(answer)
    