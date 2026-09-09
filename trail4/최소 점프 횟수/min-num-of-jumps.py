n = int(input())
num = list(map(int, input().split()))

# Please write your code here.

result = [ ]
answer = float("inf")
def backtrack(nxt_id, count):
    global answer
    if nxt_id >= n-1:
        answer = min(answer, count)
        # print(result)
        return 
    available_count = num[nxt_id]

    for i in range(1, available_count+1):
        # result.append((nxt_id, num[nxt_id]))
        backtrack(nxt_id + i, count+1)
        # result.pop()


backtrack(0, 0)



if answer == float("inf"):
    print(-1)
else:
    print(answer)
