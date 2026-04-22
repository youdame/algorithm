from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    word_length = len(begin)
    
    
    queue = deque([begin])
    n = len(words)
    visited = [False] * n
    distance = [1e9] * n 

    
    while queue:
        
        next_word = queue.popleft()
        
        if next_word == target:
            return distance[words.index(target)]
        for i in range(n):
            
            diff_count = 0
            for j in range(word_length):
                if next_word[j] != words[i][j] : 
                    diff_count += 1
   
            if diff_count == 1:
                if not visited[i]:
                    queue.append(words[i])
                    visited[i] = True
                    distance[i] = distance[words.index(next_word)] + 1 if next_word != begin else 1

    return 0