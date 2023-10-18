# while (True):
#     try:
#         a, b = map(int, input().split())
#         print(a + b)
#     except:
#         break


import sys

for x in sys.stdin:
    a, b = map(int, x.split())
    print(a+b)
