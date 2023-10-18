import sys

res = len(set([int(i) % 42 for i in sys.stdin.read().splitlines()]))
print(res)
