"""
모든 사람이 심사를 받는데 걸리는 시간을 최소로 하고싶음 

각 사람은 
선택지가 두 개인 경우 => 짧은 아저씨 선택 
하나인 경우 => 기다렸다가 짧은 아저씨 선택 or 비어있는 아저씨 선택
없는 경우 => 기다렸다가 나오는 거 or 짧은 아저씨 나올 때까지 기다리기

어떤 선택이 더 better한지 
"""

def solution(n, times):
    times.sort()
    
    left = 1
    right = 1e9 * n
    answer = 1e9
    while left <= right:
        mid = (left + right) // 2
        
        count = 0
        
        for 심사관 in times:
            count += mid // 심사관
        
        if count >= n:
            # 더 작은 mid도 가능한지
            right = mid - 1
            answer = mid
        else:
            left = mid + 1
    
    return answer
    