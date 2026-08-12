"""모든 차량이 고속도로를 이용하면서 단속 카메라를 한 번은 만나도록 설치
최대한 겹치는 부분이 많아야함

와 .. 근데 3개월 지났다고 기억 안나는 거 실화?

"""

def solution(routes):
    routes.sort(key = lambda x : x[1])
    n = len(routes)
    
    current_camera = routes[0][1]
    count = 1
    
    for i in range(n-1):
        start, end = routes[i+1]
        if start <= current_camera <= end:
            continue
        else:
            current_camera = end
            count += 1
    return count
    
