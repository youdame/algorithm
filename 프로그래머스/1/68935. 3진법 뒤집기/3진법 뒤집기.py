def solution(n):
    arr = []
    몫 = n
    while 몫 > 0:
        나머지 = 몫 % 3
        몫 //= 3
        arr.append(나머지)
    answer = 0
    print(arr)
    for i in (range(len(arr))):
        print(i, arr[i] * (3 ** i) )
        answer +=  arr[ i] * (3 ** (len(arr) - 1 - i) )
    return answer 