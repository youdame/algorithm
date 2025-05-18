
def solution(array):
    dic ={}
    for element in array:
        dic[element] = 0
    for element in array:
        dic[element] += 1
    if list(dic.values()).count(max(dic.values())) != 1:
        return -1 
    
    
    for key, value in dic.items():
        if value == max(dic.values()):
            return key
    

    