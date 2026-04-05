import sys
from collections import deque
from io import StringIO

input = sys.stdin.readline


arr = []
for _ in range(4):
    arr.append(list(map(int, input().strip())))

K = int(input())


for _ in range(K):
    num, direction = map(int, input().split())

    wheel_index = num - 1
    rotatation_directions = [0] * (4)

    rotatation_directions[wheel_index] = direction
    
    # 내 왼쪽 
    for i in range(wheel_index, 0, -1):
        cur_index = i
        left_index = i - 1
        if arr[cur_index][6] != arr[left_index][2]:
            rotatation_directions[left_index] = -rotatation_directions[cur_index]
        else:
            break
    
    # 내 오른쪽 
    for i in range(wheel_index, 3):
        cur_index = i
        right_index = i + 1
        if arr[cur_index][2] != arr[right_index][6]:
            rotatation_directions[right_index] = -rotatation_directions[cur_index]
        else:
            break

    # 회전
    for j in range(4):
        queue = deque(arr[j])
        queue.rotate(rotatation_directions[j])
        arr[j] = list(queue)
    
answer = 0
s_score = [1, 2, 4, 8]
for i in range(4):
    if arr[i][0] == 1:
        answer += s_score[i]
print(answer)
    



    