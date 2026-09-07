n = int(input())

result = []
answer = 0

def is_beautiful():
    idx = 0
    while idx < n:
        val = result[idx]  # 현재 숫자 (1, 2, 3, 4 중 하나)
        
        # 1. val만큼 뒤로 갈 칸이 남아있지 않으면 탈락 (예: 남은 칸 1개인데 숫자가 3)
        if idx + val > n:
            return False
        
        # 2. 앞으로 val개의 칸이 전부 같은 숫자(val)인지 검사
        for k in range(idx, idx + val):
            if result[k] != val:
                return False
        
        # 3. 조건을 통과했으면 해당 묶음만큼 훌쩍 건너뜀
        idx += val
        
    return True

def backtrack():
    global answer
    
    # n자리가 완성되었을 때 검사
    if len(result) == n:
        if is_beautiful():
            answer += 1
        return 

    # 1부터 4까지 뽑기 (range 끝값 주의: 1~4는 range(1, 5))
    for i in range(1, 5):
        result.append(i)
        backtrack()
        result.pop()

backtrack()
print(answer)
