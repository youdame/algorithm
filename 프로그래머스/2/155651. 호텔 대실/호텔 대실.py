def is_possible(hour, minute , new_hour, new_minute):
    return hour * 60 + minute + 10 <= new_hour * 60 + new_minute 

def solution(book_time):
    
    sorted_times = sorted(book_time, key = lambda x : x[0])
    

    N = len(sorted_times)
    visited = [False] * N
    # print(sorted_times)
    
    answer = 0
    start, end = -1, -1
    for i in range(N):
        start, end = sorted_times[i]
        
        if not visited[i]:
            visited[i] = True
            answer += 1
            
            for j in range(i, N):
                new_start, new_end = sorted_times[j]
                
                if end < new_start and not visited[j]:
                    hour, minute = int(end[0:2]), int(end[3:5])
                    new_hour, new_minute = int(new_start[0:2]), int(new_start[3:5])
                    
                    possible = is_possible(hour, minute , new_hour, new_minute)
    
                    
                    if possible:
                        start, end = sorted_times[j]
                        visited[j] = True
                        # print(i, j, visited)

    return answer