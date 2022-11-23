import random


class BingoCage:
    def __init__(self, items):
        self._items = list(items)
        # self._items가 리스트이기에 shuffle()메서드 실행 보장
        random.shuffle(self._items)

    # 핵심 메서드
    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            # self._items가 비어있으면 사용자 정의 메시지를 담은 예외 발생시킴
            raise LookupError('pick from empty BingoCage')

    # bingo.pick()에 대한 단축 형태로 bingo() 정의
    def __call__(self):
        return self.pick()


bingo = BingoCage(range(3))
print(bingo.pick())
print(bingo())
print(callable(bingo))