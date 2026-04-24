
def solution(routes):
    
    routes.sort(key = lambda x : x[1])
    count = 0
    out_camera = -30001
    for start, end in routes:
        if start <= out_camera <= end:
            continue
        else:
            out_camera = end
            count +=1 
            
    return count