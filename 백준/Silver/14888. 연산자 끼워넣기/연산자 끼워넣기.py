import sys
from io import StringIO
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))
operators_count_arr = list(map(int, input().split()))

plus_count, minus_count, multiple_count, divide_count = operators_count_arr
operators_count = sum(operators_count_arr)


max_answer = float('-inf')
min_answer = float('inf')
    
def backtracking(index, cur_val, plus, minus, mul, div):
    global max_answer,min_answer
    
    
    if index == N-1:
        min_answer = min(min_answer, cur_val)
        max_answer = max(max_answer, cur_val)
        return
        
    if plus > 0:
        backtracking(index + 1, cur_val + arr[index+1], plus-1, minus, mul, div)
        
    # elif가 아닌 이유? return 하고 나와서 그 다음 껄 계산해야해서?
    
    if minus > 0:
        backtracking(index + 1, cur_val - arr[index+1], plus, minus-1, mul, div)

        
    if mul > 0:
        backtracking(index + 1, cur_val * arr[index+1], plus, minus, mul -1, div)
    if div > 0:
        if cur_val < 0:
            cur_val = -1 * cur_val
            cal_val = cur_val  // arr[index+1] 
            cal_val *= -1
            backtracking(index + 1, cal_val, plus, minus, mul, div-1)
        else:
            backtracking(index + 1, cur_val // arr[index+1], plus, minus, mul, div-1)

        
backtracking(0, arr[0], plus_count, minus_count, multiple_count, divide_count )
print(max_answer)
print(min_answer)

