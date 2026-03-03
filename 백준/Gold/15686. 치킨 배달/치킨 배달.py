import sys 
from io import StringIO
from itertools import combinations

input = sys.stdin.readline 


N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))


def get_distance(node1, node2):
    x1, y1 = node1
    x2, y2 = node2
    return abs(x1 - x2) + abs(y1 - y2) 


chickens = []
houses = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            chickens.append((i, j))
        if arr[i][j] == 1:
            houses.append((i, j))


min_total_chicken_distance = 1e9

for comb in combinations(chickens, M):
    total_chicken_distance = 0
    chicken_distance = [[1e9] * N for _ in range(N)]

    for house in houses:
        for chicken in comb:
            distance = get_distance(chicken, house)
            k, l = house
            if distance < chicken_distance[k][l]:
                chicken_distance[k][l] = distance
    for i in range(N):
        for j in range(N):
            if chicken_distance[i][j] != 1e9:
                total_chicken_distance += chicken_distance[i][j] 
          
    min_total_chicken_distance = min(total_chicken_distance,min_total_chicken_distance)
print(min_total_chicken_distance)