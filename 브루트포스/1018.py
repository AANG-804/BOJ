import sys


def make_subboard(start_X, start_Y, board):
    temp = board[start_X:start_X+8]
    subboard = []
    for line in temp:
        subboard.append(line[start_Y:start_Y+8])
    return subboard


def count_diff(subboard):
    WB = ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW',
          'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']
    BB = ['BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB',
          'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB']
    W = []
    for idx, line in enumerate(subboard):
        W.append(sum([a != b for a, b in zip(line, WB[idx])]))
    B = []
    for idx, line in enumerate(subboard):
        B.append(sum([a != b for a, b in zip(line, BB[idx])]))
    return sum(W), sum(B)


def main():
    # 판 크기 입력 받음
    N, M = map(int, input().split())
    # 판 입력 받음
    board = sys.stdin.read().splitlines()

    if N == 8:
        startX = 0
        if M == 8:
            startY = 0
            subboard = make_subboard(startX, startY, board)
            W, B = count_diff(subboard)
            print(min(W, B))
        else:
            W, B = [], []
            for j in range(M-7):
                startX, startY = i, j
                subboard = make_subboard(startX, startY, board)
                a, b = count_diff(subboard)
                W.append(a)
                B.append(b)
            print(min(min(W), min(B)))

    else:
        if M == 8:
            startY = 0
            W, B = [], []
            for i in range(N-7):
                startX = i
                subboard = make_subboard(startX, startY, board)
                a, b = count_diff(subboard)
                W.append(a)
                B.append(b)
            print(min(min(W), min(B)))
        else:
            W, B = [], []
            for i in range(N-7):
                for j in range(M-7):
                    startX, startY = i, j
                    subboard = make_subboard(startX, startY, board)
                    a, b = count_diff(subboard)
                    W.append(a)
                    B.append(b)
            print(min(min(W), min(B)))


main()
