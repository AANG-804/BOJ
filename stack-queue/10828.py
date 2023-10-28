import sys


def stack_command(*args):
    global stack
    keyword = args[0]
    if keyword == "push":
        num = args[1]
        stack.append(num)
        return
    elif keyword == "pop":
        if not stack:
            print(-1)
            return
        else:
            last = stack.pop(-1)
            print(last)
            return
    elif keyword == "size":
        print(len(stack))
        return
    elif keyword == "empty":
        if not stack:
            print(1)
        else:
            print(0)
        return
    elif keyword == "top":
        if not stack:
            print(-1)
        else:
            print(stack[-1])
        return


lines = sys.stdin.read().splitlines()[1:]

stack = []

for line in lines:
    stack_command(*line.split())
