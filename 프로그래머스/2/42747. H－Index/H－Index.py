def solution(citations):
    n = len(citations)
    
    left = 0
    right = 10000*1000
    
    def condition(mid):
        p_count = 0
        n_count = 0
        for citation in citations:
            if citation >= mid:
                p_count += 1
            else: 
                n_count += 1
        if p_count >= mid and n_count <= mid:
            return True
        return False
        
    answer = 0
    while left <= right:
        mid = (left + right) // 2

        if condition(mid):
            # 더 큰 값도 가능한지 보기
            left = mid + 1
            
            answer = mid
        else:
            right = mid - 1
    
    return answer
            
            