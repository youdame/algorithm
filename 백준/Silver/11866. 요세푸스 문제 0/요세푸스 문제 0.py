import sys 
from io import StringIO



input = sys.stdin.readline


N, K = map(int, input().split())

arr = (list(range(1, N+1)))


i = 0

answer = []
while arr:
    i += (K - 1)
    index = i % len(arr)
    answer.append(arr[index])
    arr.pop(index)
    i = index
    
print(f"<{", ".join(map(str, answer))}>")
    
    