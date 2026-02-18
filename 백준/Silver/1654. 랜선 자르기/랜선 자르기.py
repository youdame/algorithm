import sys 

input = sys.stdin.readline

K, N = map(int, input().split()) 
arr = []
    
for _ in range(K):
    arr.append(int(input()))

# 같은 크기의 랜선을 11개 만드려고 한다
# 이분 탐색.. N개를 만들 수 있는 랜선의 최대 길이 = mid 

left = 1
right = max(arr)
answer = 0
while left <= right:
    mid = (left + right) // 2

    count = 0
    for element in arr:
        count += (element // mid)

    if count >= N:
        answer = mid
        # 더 큰 mid를 찾아봐야함
        left = mid + 1
    else:
        # 더 작은 mid를 찾아봐야함
        right = mid - 1
print(answer)
        
        
        
        
        
    


