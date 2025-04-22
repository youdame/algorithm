def solution(s):
    word = s.split(" ")
    answer = ""
    for element in word:
        for i in range(len(element)):
            if i % 2 == 1:
                answer += element[i].lower()  
            else :
                 answer += element[i].upper()  
        answer += " "
    
    return answer[:-1]