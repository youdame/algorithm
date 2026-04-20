def calculate_count(arr):
    current = arr[0]
    count = 1
    result = ""
    
    for i in range(1, len(arr)):
        if current == arr[i]:
            count += 1
        else:
            result += (current + str(count)) if count != 1 else current
            count = 1
        current = arr[i]

    result += (current + str(count)) if count != 1 else current

    return len(result)

def solution(s):
    answer = 1000
    if len(s) == 1:
        return 1
    
    for k in range(1, len(s)):
        arr = []
        split_length = k
        for i in range(0, len(s), split_length):
            arr.append(s[i:i+split_length])
        
        answer = min(answer, calculate_count(arr))
    
    return answer