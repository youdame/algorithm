"""
각 숫자 앞에 + / - 붙이기
못 만들 수도 있지 않나..?
아 그럼 그냥 0 리턴..? 

"""


def solution(numbers, target):
    answer = 0
    N = len(numbers)
    
    def cal_num(arr):
        num = 0
        for i in range(N):
            num += arr[i] * numbers[i]
        return num
    
    def dfs(arr):
        nonlocal answer
        if len(arr) == N:
            if cal_num(arr) == target:
                answer +=1
            return 
        
        for element in [1, -1]:
            arr.append(element)
            dfs(arr)
            arr.pop()

        
    dfs([])

    return answer