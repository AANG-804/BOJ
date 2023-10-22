import sys
N = [int(i) for i in sys.stdin.read().splitlines()]


def sort(N):
    for i in range(len(N)-1):
        for j in range(len(N)-i-1):
            if N[j] > N[j+1]:
                N[j], N[j+1] = N[j+1], N[j]
    return N


new_N = sort(N)

print(int(sum(new_N)/5), new_N[2], sep="\n")
