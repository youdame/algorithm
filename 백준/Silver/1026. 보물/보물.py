import sys 
from io import StringIO


input = sys.stdin.readline

N = int(input())

A_arr = sorted(list(map(int, input().split())))
B_arr = sorted(list(map(int, input().split())), reverse = True)


answer = 0
for index in range(N):
    answer += A_arr[index] * B_arr[index]

print(answer)