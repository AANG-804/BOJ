import sys
# 판 크기 입력 받음
N, M = map(int, input().split())
# 판 입력 받음
board = sys.stdin.read().splitlines()
# 정답 판임 (흰색 판, 검은 판 두가지)
WB = ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW',
      'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']
BB = ['BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB',
      'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB']

resW = []
resB = []
# 시작하는 점의 경우의 수 i, j를 모두 순회
for i in range(N-7):
    for j in range(M-7):
        resW_temp = []
        resB_temp = []
        for idx, line in enumerate(board[i:i+8]):
            resW_temp.append(
                sum([a != b for a, b in zip(line[j:j+8], WB[idx])]))
            resB_temp.append(
                sum([a != b for a, b in zip(line[j:j+8], BB[idx])]))
        resW.append(sum(resW_temp))
        resB.append(sum(resB_temp))
print(min(min(resW), min(resB)))
