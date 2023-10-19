import sys

lines = sys.stdin.read().splitlines()
words = []
max_len = 0
for line in lines:
    word = list(line)
    words.append(word)
    if max_len < len(word):
        max_len = len(word)

for i in range(max_len):
    for j in range(5):
        if i < len(words[j]):
            print(words[j][i], end="")
        else:
            print("", end="")
