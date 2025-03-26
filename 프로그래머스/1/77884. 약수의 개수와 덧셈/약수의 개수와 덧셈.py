def 약수구하기(n):
    count = 0 
    for i in range(1, n+1):
        if (n % i == 0):
            count +=1
    return count
            
    

def solution(left, right):
    sum = 0 
    for i in range(left, right+1) :
        if 약수구하기(i) % 2 == 0:
            sum += i
        else :
            sum -= i
    return sum
            