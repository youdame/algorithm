import sys
from io import StringIO

n = int(input())
arr = list(map(int, input().split())) 


"""
매일 아침에 자기가 기록한 거랑 잘 섰는지 확인함
자기보다 큰 사람이 왼쪽에 몇 명있는지만 기억함
전부다 볼 수도 있지만..

"""
current_empty_count = n
# 1번의 자리잡기

answer_arr = [-1] * n 



for i in range(n):
    me = i + 1
    left_me = arr[i]

    count = 0
    possible = False
    for j in range(n):
        if left_me == count and answer_arr[j] == -1:
            answer_arr[j] = me
            break
        if answer_arr[j] == -1:
            count += 1
print(*answer_arr)