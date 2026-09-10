n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.




answer = float("-inf")


def backtrack(count, result, start_idx):
    global answer

    if count == m:
        answer = max(answer, result)
        return 

    for i in range(start_idx, n):
        backtrack(count + 1, result ^ A[i], i + 1)
    


backtrack(0, 0, 0)

print(answer)