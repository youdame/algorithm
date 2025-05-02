
from itertools import combinations 

숫자개수, 만들어야하는수 = list(map(int, input().split()))
가진수 = list(map(int, input().split()))

# print(숫자개수, 만들어야하는수)
# print(가진수)

dictionary = {}
차이 = max(가진수)
for elements in combinations(가진수, 3):
  if(만들어야하는수 - sum(elements) >= 0 ) :
    dictionary[만들어야하는수 - sum(elements)] = sum(elements)

print(dictionary[min(dictionary)])