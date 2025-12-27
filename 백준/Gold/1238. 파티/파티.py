import sys
from io import StringIO
from queue import PriorityQueue


input = sys.stdin.readline

N, M, X = list(map(int, input().split()))

adj = [[] for i in range(N + 1)]
for i in range(M):
    A, B, W = list(map(int, input().split()))
    adj[A].append((B, W))


def 다익스트라(시작점):
    priority_queue = PriorityQueue()  # 진행 중
    distance = [1e9] * (N + 1)  # 업데이트
    distance[시작점] = 0
    priority_queue.put((0, 시작점))
    while not priority_queue.empty():
        확정가중치, 확정노드 = priority_queue.get()
        if 확정가중치 != distance[확정노드]:
            pass

        for 인접노드, 인접가중치 in adj[확정노드]:
            if distance[인접노드] > distance[확정노드] + 인접가중치:
                distance[인접노드] = distance[확정노드] + 인접가중치
                priority_queue.put((distance[인접노드], 인접노드))
    return distance


# X에서 자기 집까지의 거리 => 돌아올 때
돌아올때 = 다익스트라(X)

# 자기 집에서 X까지의 거리
for i in range(1, N + 1):
    if i == X:
        continue
    돌아올때[i] += 다익스트라(i)[X]
print(max(돌아올때[1:]))
