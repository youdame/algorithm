"""


backtracking 아닌가..?
한 알파벳만 다르면 바꿀 수 있음 -> 그걸 어케 알ㄴ지..

하나의 알파벳만 다르다 
-> 나머지는 다 같고 하나만 다르다
-> 이걸 어떻게 빨리 알지..?


"""
from collections import defaultdict

def solution(begin, target, words):

    if target not in words:
        return 0
    
    words.append(begin)
    adj = defaultdict(set)
    word_len = len(words[0])
    words_len = len(words)
    for i in range(words_len):
        i_word = words[i]
        for j in range(words_len):
            if i != j:
                j_word = words[j]
                
                count = 0
                for k in range(word_len):
                    if i_word[k] == j_word[k]:
                        count += 1
                if count == word_len-1:
                    adj[i_word].add(j_word)
                    adj[j_word].add(i_word)
                   
        
    
    answer = float("inf")
    visited = {begin}
    def backtrack(current_word, step):
        nonlocal answer
        if current_word == target:
            answer = min(step, answer)
            return 

        for next_word in adj[current_word]:
            if next_word not in visited:
                visited.add(next_word)
                backtrack(next_word, step + 1)
                visited.remove(next_word)
        
        
    backtrack(begin, 0)   
    return answer
        
            
        
        
    