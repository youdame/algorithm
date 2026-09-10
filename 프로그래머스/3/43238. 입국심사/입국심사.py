"""
심사대가 2개고 
심사관마다 처리하는 속도가 다름

비어있는 심사대를 찾는 게 관건 
일단 answer = 0

근데 그냥 각 수의 배수마다 심사대가 비는 거 아님..?
7 14 21 
10 20

아 근데 어디서 받는게 더 유리한지도 판단해야함...

"""




def solution(n, times):
    def check(mid):
    
        result = 0

        for time in times:
            result += mid // time

        if result >= n:
            return True
        return False

    left = 1
    right = max(times) * n 
    
    answer = 0
    while left <= right: 
        mid = (left + right) // 2
        if check(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer
    
    
    