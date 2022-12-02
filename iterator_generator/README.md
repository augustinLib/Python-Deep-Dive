# Iterator(이터레이터)

## Iterable object(이터러블 객체)
문자열(str), 리스트(list), 튜플(tuple), 딕셔너리(dictionary) range 객체  파이썬의 자료형들은 반복 가능하다.  



# Generator(제네레이터)
Generator(제네레이터)에 대한 간략한 정의는, **Iterator(이터레이터)** 를 만드는 함수이다.  
이러한 Generator(제네레이터)를 만드는 방법은, 함수에 `yield`키워드를 사용하는 것이다.  



## `return`과 `yield`의 차이점
다음 코드와 함께 `return`과 `yield`의 차이점을 알아보자.
```python
def func_yield():
    print("first process!")
    yield 1
    
    print("second process!")
    yield 2
    
    print("third process!")
    yield 3
```
```pycon
print(func.__next__())
first process!
1
print(func.__next__())
second process!
2
print(func.__next__())
third process!
3
```
`return`의 경우, 선언되는 순간 값을 반환함과 동시에 함수가 종료되기 때문에 값을 1개밖에 반환할 수 없다.    
그러나, 위에서의 실행 결과에서 살펴볼 수 있듯이, `yield`의 경우 각각의 부분을 나눠서 관리할 수 있기에, 여러개의 값 모두 반환이 가능하다.  
