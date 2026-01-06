# # 가장 무식하게 
N = int(input())
L = list(map(int, input().split())) #체력
J = list(map(int, input().split())) #기쁨

def solve(N, hp): # i번째 사람까지 고려했을 때, 리턴할 수 있는 최대 기쁨값 

    if N == 0: # 기저 사례 처리 # 멈추는 지점
        # hp 확인 
        # 악수를 할 경우 
        if L[N] >= hp:  
            # 불가능하다 
            cand1 = float('-inf')
        else:
            cand1 = J[N] 

        # 악수를 안 할 경우 
        cand2 = 0 # 0번째부터 0번째 사람까지 고려했을 때, 리턴할 수 있는 최대 기쁨값은, 악수를 안 하면? 기쁨값 0 
             
        return max(cand1, cand2)

    # N번째 사람과 악수를 할 수도 
    new_hp = hp - L[N]

    if new_hp <= 0: 
        cand1 = float('-inf')
    else:
        cand1 = solve(N-1, new_hp) + J[N] # N-1 번째 사람까지 고려했을 때, 최대 기쁨값의 합 

    # N번째 사람과 악수를 안 할 수도
    cand2 = solve(N-1, hp)

    # 최대 기쁨을 출력

    return max(cand1, cand2) # N 번째 까지 고려했을 때, 최대 기쁨값의 합

print(solve(N-1, 100))