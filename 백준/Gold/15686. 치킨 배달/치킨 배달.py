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
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            chickens.append((i, j))

def setting_chicken(arr, comb):
    new_arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                new_arr[i][j] = 1
    for i, j in comb:
        new_arr[i][j] = 2

    return new_arr
    
min_total_chicken_distance = 1e9
for comb in combinations(chickens, M):
    total_chicken_distance = 0
    new_arr = setting_chicken(arr, comb)
    chicken_distance = [[1e9] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if new_arr[i][j] == 2:
                for k in range(N):
                    for l in range(N):
                        if new_arr[k][l] == 1:
                            distance = get_distance((k, l), (i, j))
                            if distance < chicken_distance[k][l]:
                                chicken_distance[k][l] = distance
    for i in range(N):
        for j in range(N):
            if chicken_distance[i][j] != 1e9:
                total_chicken_distance += chicken_distance[i][j] 
          
    min_total_chicken_distance = min(total_chicken_distance,min_total_chicken_distance)
print(min_total_chicken_distance)