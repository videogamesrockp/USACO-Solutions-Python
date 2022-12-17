import sys

sys.stdin = open("paint.in", "r")
sys.stdout = open("paint.out", "w")

a, b = map(int, input().split())
c, d = map(int, input().split())

john = [x for x in range(a,b)]
bessie = [x for x in range(c,d)]

for i in john:
    if i in bessie:
        bessie.remove(i)

print(len(john) + len(bessie))