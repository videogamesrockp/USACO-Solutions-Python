"""
ID: ad41331
LANG: PYTHON3
PROG: gift1
"""
import sys
import math
sys.stdin = open ("gift1.in", "r")
sys.stdout = open ("gift1.out", "w")
N = int(input())
baldict = {}
for i in range(N):
    baldict[str(input())] = 0
for i in range(N):
    giver = str(input())
    info = list(map(int, input().split()))
    baldict[giver] -= info[0]
    if info[1] > 0:
        for j in range(info[1]):
            target = str(input())
            baldict[target] += math.floor(info[0]/info[1])
        baldict[giver] += info[0] % info[1]
for i in baldict:
    print(i, baldict.get(i))
