import sys


input = sys.stdin.readline

배열길이 = int(input())
배열 = sorted(list(map(int, input().split(" "))))


찾는개수 = int(input())
찾는배열 = list(map(int, input().split(" ")))


def is_exist(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if target == arr[mid]:
            return True
        if target <= arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return False


print(" ".join(["1" if is_exist((배열), element) else "0" for element in 찾는배열]))
