"""
소요시간이 짧은 것 => 요청 시각이 빠른 것 => 작업의 번호가 작은 것
"""

import heapq

def solution(jobs):
    jobs.sort()
    
    
    
    
    heap = []
    time, answer, count, last_idx = 0, 0, 0, 0
    while count < len(jobs):
        for i in range(last_idx, len(jobs)):
            작업번호 = i+1
            요청시간, 소요시간 = jobs[i]
            if 요청시간 <= time:
                heapq.heappush(heap, (소요시간, 요청시간, 작업번호))
                last_idx = i+1
            else:
                break
                
        if heap:
            소요시간, 요청시간, 작업번호 = heapq.heappop(heap)     
            time += 소요시간
            answer += time - 요청시간
            count += 1

        else:
            time = jobs[last_idx][0]
            
    return answer // len(jobs)
        

        
    