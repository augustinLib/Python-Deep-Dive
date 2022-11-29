def deco(func):
    def inner():
        print("running inner()")
    # deco()가 inner()함수 객체를 반환한다.
    return inner

@deco
# target()을 deco로 decorate!
def target():
    print("running target()")


# decorated된 target()을 호출하면 실제로는 inner()을 실행함
target()
# target이 inner()를 가리키고 있다.
print(target)
