def solution(n, stations, w):
    
    arr = []
    for station in stations:
        arr.append((max(station - w, 1) , min(station + w, n)))
    
    current = 1    
    influence_length = w*2 + 1
    answer = 0

    for start, end in arr:
        if current < start:
            gap = start - current

            answer += (gap // influence_length) + (1 if gap % influence_length else 0)

        current = end + 1

    if current <= n:
        gap = n - current + 1
        answer += (gap // influence_length) + (1 if gap % influence_length else 0)

    return answer