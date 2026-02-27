import sys
from io import StringIO



N = int(input())


count = 0

while N > 0:
    if len(str(N)) == 1 or len(str(N)) == 2:
        count += 1
    else:
        arr = list(map(int, list(str(N))))
        diff = []
        for i in range(len(arr) - 1):
            diff.append(arr[i+1] - arr[i])
        if len(set(diff)) == 1:
            count += 1
    N -= 1
print(count)