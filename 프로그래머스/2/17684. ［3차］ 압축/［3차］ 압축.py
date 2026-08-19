def solution(msg):
    
    record = {}
    
    for i in range(1, 27):
        record[chr(ord("A") + i - 1)] = i

    n = len(msg)
    start = 0
    answer = []
    
    while start < n:        
        end = start + 1
        
        while  end <= n and msg[start:end] in record:
            end +=1 
        
        w = msg[start : end - 1]
        answer.append(record[w])
        
        
        if end <= len(msg):
            record[msg[start:end]] = len(record) + 1


        start = end - 1
    return answer