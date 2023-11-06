from collections import deque
import sys


def VPS(string):
    ans = deque()
    for char in string:
        if char == "(":
            ans.append("(")
        elif len(ans) < 1:
            return "NO"
        else:
            ans.pop()

    if len(ans) == 0:
        return "YES"
    else:
        return "NO"


lines = sys.stdin.read().splitlines()[1:]
res = [VPS(line) for line in lines]

print(*res, sep="\n")
