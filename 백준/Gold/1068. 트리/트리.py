import sys
input = sys.stdin.readline

N = int(input())
부모들 = list(map(int, input().split()))
삭제할노드 = int(input())

# 1️⃣ 삭제할 노드와 그 자손들 전부 삭제
def delete(node):
    for i in range(N):
        if 부모들[i] == node:
            delete(i)
    부모들[node] = -2   # 삭제 표시

delete(삭제할노드)

# 2️⃣ 리프 노드 개수 세기
answer = 0
for i in range(N):
    if 부모들[i] == -2:
        continue

    # i를 부모로 가지는 노드가 있는지 확인
    is_leaf = True
    for j in range(N):
        if 부모들[j] == i:
            is_leaf = False
            break

    if is_leaf:
        answer += 1

print(answer)