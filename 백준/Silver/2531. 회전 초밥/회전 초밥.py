import sys 
from io import StringIO
from collections import deque

input = sys.stdin.readline

# 접시의 수 N, 초밥의 가짓수 d, 연속해서 먹는 접시의 수 k, 쿠폰 번호 c
N, d, k, c = map(int, input().split()) 

# 초밥의 종류
arr = []

for _ in range(N):
    arr.append(int(input()))
    



left = 0
right = k

new_arr = deque(arr[left:right])
answer_arr = list(new_arr)
answer_arr.append(c)

answer = len(set(answer_arr))
while left < len(arr):
    new_element = arr[(right) % len(arr)]

    new_arr.append(new_element)
    new_arr.popleft()

    answer_arr = list(new_arr)
    answer_arr.append(c)
    answer = max(len(set(answer_arr)), answer)
    left += 1
    right += 1

# 회전 초밥 벨트에서 먹을 수 있는 초밥의 가짓수의 최댓값

print(answer)