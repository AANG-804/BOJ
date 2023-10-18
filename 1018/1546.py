import sys

a = sys.stdin.read().splitlines()
scores = [int(i) for i in a[1].split()]
m = max(scores)
new_scores = [i/m*100 for i in scores]
print(sum(new_scores)/int(a[0]))
