import sys
from io import StringIO


input = sys.stdin.readline

통나무수, 내가원하는미터 = map(int, input().split(" "))
통나무들 = sorted(list(map(int, input().split(" "))))


def find():
    left = 0
    right = max(통나무들)
    answer = 0
    while left <= right:
        mid = (left + right) // 2

        합 = sum([element - mid for element in 통나무들 if element > mid])

        if 합 >= 내가원하는미터:
            answer = mid
            left = mid + 1

        else:
            right = mid - 1
    return answer


print(find())
