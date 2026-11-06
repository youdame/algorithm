from collections import defaultdict
def solution(user_id, banned_id):
    record = defaultdict(list)
    m = len(banned_id)
    k = len(user_id)
    # banned_id 요소마다 
    for banned_index in range(m):
        key = banned_id[banned_index]
        
        n = len(key)
        star_index_set = set()
        
        # *이 들어간 곳
        for index in range(n):
            if key[index] == "*":
                star_index_set.add(index)
        
        # 각 user_id와 비교
        for value in user_id:
            is_match = True
            if len(key) != len(value):
                continue
            for id_index in range(n):
                if id_index in star_index_set:
                    continue
                if key[id_index] != value[id_index]:
                    is_match = False

            if is_match:
                record[banned_index].append(value)
    print(record)
    
    visited = set()
    
    answer = set()
    
    def dfs(index):
        nonlocal answer
        if index == m and len(visited) == m:
            # print(visited)
            answer.add(tuple(sorted(visited)))
            return 
        # banned_id 인덱스 하나씩 돌면서 

        # 해당되는 인덱스의 매칭된 value들 
        for matched_id in record[index]:
            # 방문 안햇으면 
            if matched_id not in visited:
                visited.add(matched_id)
                dfs(index + 1)
                visited.remove(matched_id)

                
    dfs(0)
    return len(answer)
    