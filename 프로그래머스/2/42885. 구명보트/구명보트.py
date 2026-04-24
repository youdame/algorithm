def solution(people, limit):
    people.sort()
    n = len(people)
    left = 0 
    right = n - 1

    
    count = 0
    
    while left <= right:
        
        무거운놈 = people[right]
        
        남은무게 = limit - 무거운놈
        
        if 남은무게 < people[left]:
            right -= 1
        else:
            right -= 1
            left += 1
        count += 1
        
        # print(left, right, count)
    return count