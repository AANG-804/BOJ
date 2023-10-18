import sys

N = [int(n) for n in sys.stdin.read().splitlines()]
m = max(N)
print(m, N.index(m)+1, sep="\n")
