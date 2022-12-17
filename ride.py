"""
ID: ad41331
LANG: PYTHON3
PROG: ride
"""
import sys
sys.stdin = open ("ride.in", "r")
sys.stdout = open ("ride.out", "w")
comet = map(ord, [*input()])
comet = [i - 64 for i in x]
cometproduct = 1
for i in x:
    cometproduct*=i
group = map(ord, [*input()])
group = [i - 64 for i in y]
groupproduct = 1
for i in y:
    groupproduct*=i
if groupproduct % 47 == cometproduct % 47:
    print("GO")
else:
    print("STAY")
