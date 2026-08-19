def solution(s):
    n = len(s)
    
    answer = n
    answer_str = ""

    for i in range(1, n):
        prev = s[0:i]
        count = 1
        

        str_value = ""
        
        for j in range(i, n, i):
            if prev == s[j:j+i]:
                count += 1
            else:
                
                if count != 1:
                    str_value += f"{count}{prev}"
                else:
                    str_value += f"{prev}"
                prev = s[j:j+i]
                count = 1

        if count != 1:
            str_value += f"{count}{prev}"
        else:
            str_value += f"{prev}"
            
        if len(str_value) < answer:
            answer = len(str_value)
            answer_str = str_value
    return answer
            