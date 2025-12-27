import sys
from io import StringIO
from queue import PriorityQueue

input = sys.stdin.readline

V, E = list(map(int, input().split()))
K = int(input())


adj = [[] for i in range(V + 1)]
for i in range(E):
    u, v, w = list(map(int, input().split()))
    adj[u].append((v, w))

INF = float("inf")
priority_queue = PriorityQueue()  # 개발
distance = [INF] * (V + 1)  # 확정


##############################
def 다익스트라():
    while not priority_queue.empty():
        뽑은거리, 뽑은노드 = priority_queue.get()
        if 뽑은거리 > distance[뽑은노드]:
            continue
        for new_node, weight in adj[뽑은노드]:
            if distance[new_node] > distance[뽑은노드] + weight:
                distance[new_node] = distance[뽑은노드] + weight
                priority_queue.put((distance[new_node], new_node))


priority_queue.put((0, K))
distance[K] = 0


다익스트라()
for index in range(1, len(distance)):
    print("INF" if distance[index] == INF else distance[index])
