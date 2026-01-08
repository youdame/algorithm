import sys
from io import StringIO

input = sys.stdin.readline


arr = [i + 1 for i in range(int(input()))]

new_arr = []

while len(arr) > 1:
    for index in range(1, len(arr), 2):
        new_arr.append(arr[index])
    arr = new_arr
    new_arr = []
print(arr[0])
