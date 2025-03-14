import math
def solution(n):
    문자제곱근 = str(math.sqrt(n))
    
    if 문자제곱근.split(".")[1] == '0':
        제곱근 = 문자제곱근.split(".")[0]
        return (int(제곱근) + 1) * (int(제곱근) + 1)
    else:
        return -1
        