def maxNum(n, m):
    max_val = 1
    for i in range(1, min(n, m)+1):  # 공약수는 1부터 작은 수까지
        if n % i == 0 and m % i == 0:
            max_val = i
    return max_val

def minNum(n, m):
    for i in range(max(n, m), n * m + 1):  # 최소공배수는 최대 n*m까지 존재 가능
        if i % n == 0 and i % m == 0:
            return i
    return n * m

def solution(n, m):
    return [maxNum(n, m), minNum(n, m)]
