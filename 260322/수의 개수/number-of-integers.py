n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [int(input()) for _ in range(m)]

# Please write your code here.

def upper_bound(target):

    left = 0
    right = n - 1
    answer = n

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > target:
            right  = mid - 1
            answer = mid
        else:
            left = mid + 1

    return left 


def lower_bound(target):
    left = 0
    right = n - 1
    answer = n
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            right  = mid - 1
            answer = mid
        else:
            left = mid + 1       

    return left 


def binary_search(target):
    left = 0
    right = n - 1


    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid 
        elif arr[mid] > target:
            right = mid - 1 
        else:
            left = mid + 1       

    return -1 


for target in queries:
    
    upper = upper_bound(target)
    lower = lower_bound(target)
    # print(upper, lower)
    if binary_search(target) == -1:
        print(0)
    else: 
        print(upper - lower)