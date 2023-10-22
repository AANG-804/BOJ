# 덱을 입력받는다
N, M = map(int, input().split())
deck = [int(i) for i in input().split()]
# 덱에서 3개의 카드로 조합할 수 있는 카드를 모두 뽑는다.
# 뽑은 카드가 3장이 될때까지 카드를 한장 뽑는다
res = []


def draw(now, left):
    # 현재 뽑은 카드가 세 장일 때 탈출
    if (len(now) > 2):
        s = sum(now)
        if (M-s >= 0):
            res.append(s)
    else:
        # 남아있는 카드를 한장씩 뽑음
        for card in left:
            new_now, new_left = now.copy(), left.copy()
            # 뽑은 카드를 now로 옮김
            new_now.append(card)
            new_left.remove(card)
            draw(new_now, new_left)


draw(list(), deck)
print(max(res))


# 3개의 카드로 만든 숫자중 가장 M과 가까운 수를 선택한다.
