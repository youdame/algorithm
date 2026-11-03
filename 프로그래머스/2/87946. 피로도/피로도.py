def solution(k, dungeons):
    
    n = len(dungeons)
    
    arr = []
    
    answer = 0
    def dfs(피로도):
        nonlocal answer
        answer = max(answer , len(arr))
        if 피로도 <= 0:
            answer = max(answer , len(arr))
            return 

        for i in range(n):
            if i not in arr:
                최소피로도, 소모피로도 = dungeons[i]
                # print(최소피로도, 소모피로도)
                if 최소피로도 <= 피로도 :
                    arr.append(i)
                    dfs(피로도 - 소모피로도)
                    arr.pop()
                
    dfs(k)
    return answer