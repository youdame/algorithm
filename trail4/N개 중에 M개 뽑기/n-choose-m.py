N, M = map(int, input().split())

# Please write your code here.




def backtrack(result, start):

    if len(result) == M :
        print(" ".join(map(str, result)))
        return 

    for i in range(start + 1, N + 1):

        result.append(i)
        backtrack(result, i)
        result.pop()



backtrack([], 0)
