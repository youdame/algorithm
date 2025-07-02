import sys

input = sys.stdin.readline
n = int(input())

for i in range(n, 0, -1):
    if all(j == "7" or j == "4" for j in str(i)):
        print(i)
        exit()
