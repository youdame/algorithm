K, N = map(int, input().split())

# Please write your code here.


result = []

def backtrack():
    global result
    if len(result) == N:
        print(" ".join(map( str,result)))
        return 
    for i in range(1, K+1):
        result.append(i)
        backtrack()
        result.pop()
    

backtrack()
