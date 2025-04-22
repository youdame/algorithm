def lastFound(s, target):
    return s.rfind(target)

def solution(s):
    arr= []
    for i in range(len(s)):
        target = s[i]
        if s.find(target) == i:
             arr.append(-1)
        else :
            last = lastFound(s[0:i], target)
            arr.append( i -last)
    return arr