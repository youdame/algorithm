from collections import deque

def solution(begin, target, words):
    n = len(words)
    visited = [False] * n
    queue = deque([(begin, 0)])
    
    while queue:
        current_node, current_dist = queue.popleft()
        
        if current_node == target:
            return current_dist
        
       
        for word in words:
            miss_count = 0
            for i in range(len(word)):
                if word[i] != current_node[i]:
                    miss_count += 1
            word_index = words.index(word)
            
            if miss_count == 1 and not visited[word_index]:
                queue.append((word, current_dist + 1))
                visited[word_index] = True
                
    return 0
