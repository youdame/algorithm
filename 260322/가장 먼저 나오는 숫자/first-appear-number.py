n, m = map(int, input().split())
arr = list(map(int, input().split()))
query = list(map(int, input().split()))

# Please write your code here.

def lower_bound(target):
    left = 0
    right = n - 1
    answer = n

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer


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


for target in query:
    if binary_search(target)  == -1:
        print(-1)
    else:
        print(lower_bound(target) + 1)
