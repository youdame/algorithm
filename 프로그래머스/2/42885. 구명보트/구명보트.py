def solution(people, limit):
    people.sort()
    
    # print(people)

    n = len(people)
    
    left = 0
    right = n - 1
    
    answer = 0
    while left <= right:
        if people[left] + people[right] > limit:
            right -= 1
        else:
            right -= 1
            left += 1
        answer += 1
    return answer
    