import sys
from io import StringIO
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
n, m = list(map(int, input().strip().split(" ")))
parents = list(map(int, input().strip().split(" ")))

# 0번 무시
점수판 = [0] * (n + 1)
# 0번 무시
children = [[] for _ in range(n + 1)]
for i in range(len(parents)):  # 다 도는 중
    나 = i + 1
    부모 = parents[i]
    if 부모 != -1:
        children[부모].append(나)


def 타고들어가기(현재노드):
    for 자식 in children[현재노드]:
        점수판[자식] += 점수판[현재노드]
        타고들어가기(자식)


for j in range(m):
    i, w = list(map(int, input().strip().split(" ")))
    점수판[i] += w
타고들어가기(1)
print(" ".join(map(str, 점수판[1:])))
