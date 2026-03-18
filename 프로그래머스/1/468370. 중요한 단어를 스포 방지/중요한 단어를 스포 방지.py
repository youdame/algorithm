def solution(message, spoiler_ranges):
    
    # 1️⃣ 일반 구간 단어 구하기
    def get_not_importants(message, spoiler_ranges):
        n = len(message)
        is_spoiled = [False] * n
        
        for s, e in spoiler_ranges:
            for i in range(s, e+1):
                is_spoiled[i] = True
        
        not_importants = set()
        i = 0
        
        while i < n:
            if message[i] == ' ':
                i += 1
                continue
            
            start = i
            while i < n and message[i] != ' ':
                i += 1
            end = i - 1
            
            has_spoiler = False
            for j in range(start, end+1):
                if is_spoiled[j]:
                    has_spoiler = True
                    break
            
            if not has_spoiler:
                not_importants.add(message[start:end+1])
        
        return not_importants

    # 2️⃣ 스포 구간 → 단어 확장
    def get_complete_word(s, e, message):
        n = len(message)
        
        while s > 0 and message[s-1] != ' ':
            s -= 1
        
        while e < n-1 and message[e+1] != ' ':
            e += 1
        
        return message[s:e+1].strip()
    
    not_importants = get_not_importants(message, spoiler_ranges)
    importants = set()
    
    # 3️⃣ 각 스포 구간 처리
    for s, e in spoiler_ranges:
        
        word_block = get_complete_word(s, e, message)
        words = word_block.split()
        
        for w in words:
            if w not in not_importants:
                importants.add(w)
    
    return len(importants)