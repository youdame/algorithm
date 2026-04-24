def solution(routes):
    routes.sort(key=lambda x: x[1])
    
    arr = []
    for route in routes: # 통째로 가져온 뒤
        start = route[0] # 인덱스로 꺼내기
        end = route[1]
        
        if arr and start <= arr[-1] <= end:
            continue
        else:
            arr.append(end)
            
    return len(arr)