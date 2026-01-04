import sys
from io import StringIO
from collections import deque


input = sys.stdin.readline
T = int(input())
for i in range(T):
    fun = input().strip()
    n = int(input())
    arr = input().strip()
    empty = False
    if len(arr) == 2:
        empty = True
    arr = arr[1 : len(arr) - 1].split(",")
    arr = deque(map(int, arr)) if not empty else []
    reverse = False
    error = False
    for method in fun:
        if method == "R":
            reverse = not reverse
        if method == "D":
            if arr:
                if reverse:
                    arr.pop()
                else:
                    arr.popleft()
            else:
                error = True
    answer = "["
    if error:
        print("error")
    else:
        if reverse:
            for index in range(len(arr) - 1, -1, -1):
                answer += str(arr[index])
                if index != 0:
                    answer += ","
        else:
            for index in range(len(arr)):
                answer += str(arr[index])
                if index != len(arr) - 1:
                    answer += ","
        print(answer + "]")
