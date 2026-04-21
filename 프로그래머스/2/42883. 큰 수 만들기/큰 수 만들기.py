"""
뭘 제거했다는거지..?
k개의 숫자를 제거했을 때 얻을 수 있는 가장 큰 숫자...


1924 
뭘 제거해..?

각각이 독립된 숫자임..
가운데를 제거할 수도 있음

근데 순서를 바꾸진 못함.. 정렬 불가능
"4177252841"
=> 775841

만들 수 있는 가장 큰ㅅ ㅜ..

그리디고 뭐고 생각하지말고 완탐으로 구현한다면 어떻게 할 수 있을까?

1924 -> 2개 빼기 조합으로 2개 제거 ? -> 터짐
제거하는 숫자의 크기가 작을수록 좋다..?

남아있는 숫자가 앞쪽에 있는 애는 숫자가 크면 좋음..?
인덱스, 숫자 쌍으로 저장한 다음 
인덱스는 움직일 수 없음..
숫자는 

1231234

2334

4177252841

1122445778

우리 중에 제일 큰 애가 앞으로 와야하는데..?
제일 큰 애가 앞으로 올 수 있는 상황이 안될 수도,..?




"""


def solution(number, k):
    stack = []
    
    for str_number in number:
        current_num = int(str_number)
        
        if k == 0:
            stack.append(current_num)
            continue
        
        while stack and stack[-1] < current_num:
            stack.pop()
            k -= 1
            if k == 0:
                break
        stack.append(current_num)
    if k > 0:
        stack = stack[:-k]
    return "".join(map(str, stack))