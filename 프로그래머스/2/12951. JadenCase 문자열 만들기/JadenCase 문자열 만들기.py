def solution(s):
    arr = s.split(" ")
    arr2 = []
    for i in arr:
        문자 = i
        if 문자 == "":
            arr2.append(문자)
            continue
        else:
            첫글자 = 문자[0].upper()
            나머지 = 문자[1:].lower()
            arr2.append(첫글자+나머지)
        
    return " ".join(arr2)