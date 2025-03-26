def solution(numbers):
    sum = 0
    list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    for i in list:
        if i not in numbers:
            sum += i
            
    return sum
