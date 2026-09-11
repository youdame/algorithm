
n = int(input())
grid = [list(input()) for _ in range(n)]

# Please write your code here.

answer = float("inf")

start = ()
end = ()
record = {}
for i in range(n):
    for j in range(n):
        if grid[i][j] == "S":
            start = (i, j)
        if grid[i][j] == "E":
            end = (i, j)
        if grid[i][j].isdigit():
            record[int(grid[i][j])] = (i, j)



def get_distance(r1, c1, r2, c2):
    return abs(r1-r2 ) + abs(c2-c1)


possible_combination = []
path = []
def combination(idx):
    if len(path) == 3:
        possible_combination.append(list(path))
        return 
    for i in record.keys():
        if i > idx:
            path.append(i)
            combination(i)
            path.pop()


combination(0)


sr, sc = start
er, ec = end
if not possible_combination:
    print(-1)

else:
    for a, b , c in possible_combination:
        r1, c1 = record[a]
        r2, c2 = record[b]
        r3, c3 = record[c]
        answer = min(answer, get_distance(sr, sc, r1, c1) + get_distance(r1, c1, r2, c2) + get_distance(r2, c2, r3, c3) + get_distance(er, ec, r3, c3))
    print(answer)