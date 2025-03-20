def solution(arr):
    if not arr:
        return []
    
    result = [arr[0]]  # 첫 번째 원소는 무조건 포함
    
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:  # 이전 원소와 다를 때만 추가
            result.append(arr[i])
    
    return result