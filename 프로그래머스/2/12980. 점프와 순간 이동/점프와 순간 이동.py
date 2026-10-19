"""
1) k칸을 앞으로 점프 -> 건전지 K만큼 사용
2) 현재까지 온 거리 * 2 순간이동  -> 건전지 사용 X

점프는 최소화하면서 이동하려고 함


"""

def solution(n):
    
    # 최대한 순간이동을 많이 쓰고, 최소한으로 점프를 씀
    answer = 0
    loc = n
    

    while loc > 0:
 
        # 순간이동, 건전지 사용 x
        if loc % 2 == 0:
            loc = loc // 2
        
        # 점프, 건전지 사용
        else:
            loc -= 1
            answer += 1
        # print(loc)

    return answer