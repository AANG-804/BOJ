from operator import itemgetter
import sys

users = [s.split()+[i] for i, s in enumerate(sys.stdin.readlines()[1:])]

for user in users:
    user[0] = int(user[0])

users = sorted(users, key=itemgetter(0, 2))
for user in users:
    print(user[0], user[1])
