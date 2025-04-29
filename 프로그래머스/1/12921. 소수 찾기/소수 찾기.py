def solution(n):
    count = 0
    for i in range(2, n+1):
        if 소수찾기(i):
            count+=1
    return count

def 소수찾기(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True