def solution(s, n):
    answer = ""
    for element in s: 
        if element == " ":
            answer += " "
            continue 
        if element.isupper():
            answer += chr((ord(element) - ord('A') + n ) % 26 + ord('A'))
        elif element.islower():
            answer += chr((ord(element) - ord('a') + n) % 26  + ord('a'))
    
    return answer
