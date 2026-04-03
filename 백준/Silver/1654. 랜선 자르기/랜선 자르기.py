import sys
from io import StringIO


input = sys.stdin.readline

"""
N개의 랜선을 만들어야하는데, 현재 K개만 있음 

K <= N 이겠네?

K를 잘라서 N개를 만들어야함 
N개는 모두 같은 길이임

N이 가장 크게 랜선을 자르려고 할 때, N이 가장 큰 경우 

딱봐도 이분탐색 .. 
"""
K, N = map(int, input().split())

lensuns = []
for i in range(K):
    lensuns.append(int(input()))


left = 1
right = max(lensuns)


def cal_lensun_count(lensun_length):
    count = 0
    for element in lensuns:
        count += element // lensun_length

    return count

answer = -1e9
while left <= right:
    mid = (left + right) // 2

    count = cal_lensun_count(mid)

    # N개보다 더 많이 만들거나 N개를 만든 경우 => 더 가능한 지 보기 => mid는 크면 클수록 좋으므로 mid를 더 늘려보기
    if count >= N:
        answer = max(mid, answer)
        left = mid + 1
    else:
        # N개보다 적게 만든 경우 => 너무 mid가 큼 => 줄여야함 
        right = mid - 1
print(answer)
