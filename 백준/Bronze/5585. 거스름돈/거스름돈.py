import sys
from io import StringIO
from collections import defaultdict


change_coins = defaultdict()

N = int(input())

coins= [500, 100, 50, 10, 5, 1]

change = 1000 - N

for coin in coins:
    change_coins[coin] = change // coin
    change = (change - coin * change_coins[coin])


print(sum(change_coins.values()))