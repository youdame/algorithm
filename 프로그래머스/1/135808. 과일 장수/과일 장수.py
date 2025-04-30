def solution(k, m, score):
    
    # 이익 = 최저사과점수 * 한상자에담긴사과개수 * 상자개수
    총상자수 = len(score) // m
    # 한상자에담긴사과개수 = len(score) // k
    # print(총상자수,한상자에담긴사과개수)
    # print(list(reversed(sorted(score))))
    answer = 0
    뒤집은배열 =list(reversed(sorted(score)))
    for i in range(총상자수):
        한상자 = 뒤집은배열[i*m:(i+1)* m]
        answer += min(한상자) * m
    return answer
    