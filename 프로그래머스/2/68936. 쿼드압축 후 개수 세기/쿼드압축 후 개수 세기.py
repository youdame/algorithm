"""
len(arr)을 2로 나눈만큼 반복


절반을 확인하면 됨
4 -> 2 -> 1
8 -> 4 -> 2 -> 1

and 연산? 

"""



def solution(arr):
    answer = [0, 0]
    def 압축가능여부(x, y, length):
        possible = True        
        start = arr[x][y]
        for i in range(x, x + length):
            for j in range(y, y + length):
                if start != arr[i][j]:
                    possible = False
        return possible
    
    def dfs(x, y, length):

        possible = 압축가능여부(x, y, length)
        if possible:
            answer[arr[x][y]] += 1        
            if length == 1:
                return 
        else:
            dfs(x, y, length // 2)
            dfs(x + length // 2, y, length // 2)
            dfs(x, y+ length // 2, length // 2)
            dfs(x + length // 2, y + length // 2, length // 2)


    
    dfs(0, 0, len(arr))
    
    return answer

    