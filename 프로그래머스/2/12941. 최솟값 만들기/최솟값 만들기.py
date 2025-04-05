def solution(A,B):
    sum=0
    A.sort(reverse=True)
    B.sort()
    for i in range(len(A)):
        a = A[-1]
        b = B[-1]
        print(a,b)
        sum += a * b
        A.pop()
        B.pop()
    return sum
        