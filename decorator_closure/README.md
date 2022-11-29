# Decorator
decorator는 다른 함수를 인수로 받는 callable이다.  
decorator는 decorated된 함수에 특정 처리를 수행하고, 함수를 반환하거나 함수를 다른 함수나 callable 객체로 대체한다.  
예제와 함께 살펴보겠다.  
```python
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

```