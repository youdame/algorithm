import sys
from io import StringIO


input = sys.stdin.readline

N = int(input())
candies = []
for _ in range(N):
    candies.append(list(input().strip()))

def 검사(arr):
    max_row_answer = -1e9
    row_answer = 1
    
    for i in range(N):
        for j in range(N-1):
            if arr[i][j] == arr[i][j+1]:
                row_answer += 1   
            else:
                row_answer = 1
            max_row_answer = max(row_answer, max_row_answer)
        row_answer = 1
            
    max_col_answer = -1e9
    col_answer = 1
    for j in range(N):
        for i in range(N-1): 
            if arr[i][j] == arr[i+1][j]:
                col_answer += 1
            else:
                col_answer = 1
            max_col_answer = max(col_answer, max_col_answer)
        col_answer = 1
    return max(max_row_answer, max_col_answer)

                
new_candies = [row[:] for row in candies]

max_row_value = 검사(new_candies)
# 색이 다를 때 행을 교체 
for i in range(N):
    for j in range(N-1):
        if new_candies[i][j+1] != new_candies[i][j]:
            temp = new_candies[i][j+1]
            new_candies[i][j+1] = new_candies[i][j]
            new_candies[i][j] = temp
            # 검사, 행// 열 다 함
            value = 검사(new_candies)
            max_row_value = max(value, max_row_value)
            # 되돌리기
            new_candies = [row[:] for row in candies]


# 열을 교체
max_col_value = 검사(new_candies)
for i in range(N-1):
    for j in range(N):
        if new_candies[i+1][j] != new_candies[i][j]:
            temp = new_candies[i+1][j]
            new_candies[i+1][j] = new_candies[i][j]
            new_candies[i][j] = temp
            # 검사, 행// 열 다 함
            value = 검사(new_candies)
            max_col_value = max(value, max_col_value)
            # 되돌리기
            new_candies = [row[:] for row in candies]
print(max(max_row_value, max_col_value))

