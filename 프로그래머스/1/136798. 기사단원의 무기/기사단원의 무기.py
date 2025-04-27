def 약수개수(n):
    count = 0 
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            if i * i == n:
                count +=1
                continue
            count += 2
    return count 

def solution(number, limit, power):
    return(sum([power if 약수개수(i) > limit else 약수개수(i) for i in range(1, number+1)] ))