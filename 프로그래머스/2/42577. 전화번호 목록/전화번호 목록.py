"""
n은 1e6

정렬하면 비슷한 것끼리 앞에 가있지 않나..?

투포인터 이런 건가..?

접두어인 경우가 있으면 false

사실 다 확인을 해봐야 true를 리턴할 수 잇ㅇ므

효율적으로 확인하는 방법이 있을까?
정렬을 하면 비슷한 애들끼리 가까이에 있음..
"""

def solution(phone_book):
    phone_book.sort(key=lambda x :(x, len(x)))
    
    answer = True
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            answer = False
            return answer
    return answer