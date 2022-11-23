# function(함수)

## 목차
[1. parameter(매개변수)]()
[2. lambda(람다 함수)](#lambda(람다-함수))

## parameter(매개변수)
### positional parameter(위치 매개변수)
- 가장 기본적인 매개변수이다.  
- 함수를 호출할 때 순서대로 데이터(인자)를 넘겨줘야 한다.
- 다른 매개변수와 함께 쓸 때는 항상 맨 앞에 써야 한다.
```python
def my_func(a, b):
    print(a, b)


# 인자가 1, 2가 순서대로 a와 b에 넘겨짐을 확인할 수 있다.
my_func(1, 2)
```

### default parameter(기본 매개변수)
- 매개변수의 default값
- 함수를 정의할 때 매개변수의 기본 값을 지정할 수 있다.
```python
# default parameter
# content 매개변수의 default값 지정
def info(title, content='no contents'):
    print(f'제목 : {title}')
    print(f"내용 : {content}")


# content 인자에 값을 지정하지 않았기 때문에 default값 출력
info("test")
```

### keyword parameter(키워드 매개변수)
- 함수 호출 시에 키워드를 붙여 호출한다
- 매개변수의 순서를 지키지 않아도 된다
```python
# keyword parameter
def info(title, content):
    print(f'제목 : {title}')
    print(f"내용 : {content}")


# 키워드를 붙여 호출하기 때문에 매개변수의 순서를 지키지 않아도 된다
info(content="None", title="test")
```

### positional variable length parameter(위치 가변 매개변수)
- 가변 매개변수 = 개수가 정해지지 않은 매개변수
- 매개변수 앞에 *이 붙는다(tuple)
```python
# positional variable length parameter
# 가변 매개변수 = 개수가 정해지지 않은 매개변수
# 매개변수 앞에 *이 붙음을 확인할 수 있다.
def fruits(*args):
    for arg in args:
        print(arg)


# 매개변수들이 tuple로 묶여서 args로 들어가게 됨
fruits('apple', 'orange', 'mango')
```

### keyword variable length parameter(키워드 가변 매개변수)
- 가변 매개변수 = 개수가 정해지지 않은 매개변수
- 매개변수 앞에 **이 붙는다(dictionary)
```python
# keyword variable length parameter(키워드 가변 매개변수)
# 가변 매개변수 = 개수가 정해지지 않은 매개변수
# 매개변수 앞에 **이 붙음을 확인할 수 있다.
# kwargs : keyword argument의 줄임말
def fruit_price(**kwargs):
    # dictionary
    for key, value in kwargs.items():
        print(f"{key} : {value}")


# 매개변수들이 dictionary로 묶여서 kwargs로 들어가게 됨
fruit_price(apple=1200, orange=2900, mango=3100)
```

### 매개변수 작성 순서
> 위치 - 기본 - 위치 가변 - 키워드 - 키워드 가변

```python
def example_func(positional, default="default", *args, **kwargs):
    return -1
```

---

## lambda(람다 함수)
- 이름을 지을 필요가 없는 간단한 형태의 함수
- 다른 함수의 인자(argument)로 넣을 수 있다
- 코드가 간결해지고, 메모리가 절약되는 장점이 있다

### 람다 함수의 정의
```python
# define lambda
# lambda parameter : result
plus_one = lambda x: x + 1

# call lambda
print((lambda x: x + 1)(2))
print(plus_one(1))
```

### 람다 함수와 조건문
```python
# lambda와 조건문
# lambda로 if statement 사용 시, else statement까지 필수적으로 사용해야함
print((lambda x: True if x > 0 else False)(3))
```

---

## map, filter 함수
### map 함수 사용법
```python
# map(함수, 순서가 있는 자료형)
map(int, ["3", "4", "5", "6"])
# return : map object

list(map(int, ["3", "4", "5", "6"]))
```
### map 함수 활용
```python
# 리스트 각 요소 공백 지우기
def strip_all(x):
    return x.strip()


items = [' el1', ' el2 ']
# map(함수, 순서가 있는 자료형)
items = list(map(strip_all, items))

# 람다 함수와 함께 활용
items = [' el1', ' el2 ']
items = list(map(lambda x: x.strip(), items))
```

### filter 함수 사용법
```python
# filter(함수, 순서가 있는 자료형)
def func(x):
    return x < 0


# return : filter object


list(filter(func, [-3, -2, 0, 5, 7]))
```

---

## 일급 객체로서의 함수(일급 함수)
**파이썬의 함수는 일급 객체이다.** 일급 객체는 다음과 같은 특징을 지닌다.
- 런타임에 생성할 수 있다.
- 데이터 구조체의 변수나 요소에 할당할 수 있다.
- 함수 인수로 전달할 수 있다.
- 함수 결과로 반환할 수 있다.

정수, 문자열, 딕셔너리와 같은 요소들도 일급 객체이다.  


### 객체로서의 함수
아래의 파이썬 콘솔을 살펴보면서 일급 객체로서의 함수의 특징을 살펴보자(not script)
```pycon
>>> def add_2(x):
...    '''return x+2'''
...    return x+2

>>> add_2(3)
5

>>> add_2.__doc__
'return x+2'

>>> type(add_2)
<class 'function'>
```
- 파이썬 콘솔 세션에 있기 때문에, 현재 함수를 런타임에 생성하는 것이다.
- `__doc__`은 함수 객체의 속성 중 하나이다.
- `add_2`는 function 클래스의 객체이다.


아래에서 이어서 살펴보겠다.
```pycon
>>> add2 = add_2

>>> add2
<function add_2 at 0x10646eb90>

>>> add2(4)
6

>>> list(map(add2, range(9)))
[2, 3, 4, 5, 6, 7, 8, 9, 10]
```
- add_2 함수를 add2 변수에 할당하였고, 변수명을 통해 함수를 호출하였다.
- 이러한 변수를 map()의 인자로 전달하였다.

### 고위 함수(higher-order function)
**고위 함수(higher-order function)란, 함수를 인수로 받거나 함수를 결과로 반환하는 함수를 말한다.**  
대표적인 예시로는 `map()`, `sorted()`가 있다. sorted 함수는 선택적인 key 인수로 함수를 전달받아 정렬 대상에 적용한다.
```pycon
>>> fruits = ['watermelon', 'melon', 'strawberry', 'apple']
>>> sorted(fruits, key=len)
['melon', 'apple', 'watermelon', 'strawberry']

def reverse(word):
    return word[::-1]
sorted(fruits, key=reverse)
['apple', 'melon', 'watermelon', 'strawberry']
```


### 익명 함수
`lambda` 키워드는 파이썬 표현식 내에 익명 함수를 생성한다.  
이 때, 람다 함수의 본체는 순수한 표현식으로만 구성되도록 제한된다.  
즉, 람다 본체에서는 할당문이나, while, try 등의 파이썬 문장을 사용할 수 없다.  
이러한 람다 함수는 위에서 언급한 고위 함수 안의 인자로써 유용하게 사용된다.
```pycon
>>> fruits = ["strawberry", "apple", "banana", "orange"]
>>> sorted(fruits, key = lambda word : word[::-1])
['banana', 'orange', 'apple', 'strawberry']
```
고위 함수 예시에서의 과일 이름 마지막 글자 기준 정렬이다. 
`lambda` 키워드를 통해 간편하게 sorted() 함수를 이용할 수 있다.  

## Callable 객체
호출 연산자인 `()`는 사용자 정의 함수 이외의 다른 객체에도 사용할 수 있다.  
호출할 수 있는 객체(Callable)인지 알아보려면 `callable()`내장 함수를 사용한다.  
파이썬에는 다음과 같은 callable이 있다.
- ### 사용자 정의 함수  
  def 문이나 람다 표현식으로 생성
- ### 내장 함수  
  `len()`이나 `time.strftime()`처럼 C언어로 구현된 함수
- ### 내장 메서드
  `dict.get()`처럼 C언어로 구현된 메서드
- ### 메서드
  클래스 본체에 정의된 함수
- ### 클래스
  호출될 때 클래스는 자신의 `__new__()`메서드를 실행해서 객체를 생성하고, `__init__()`으로
초기화한 후, 최정적으로 호출자에 객체를 반환한다. 파이썬에서는 new 연산자가 없기 때문에 클래스를 호출하는 것은 
함수를 호출하는것과 동일하다.(일반적으로 클래스를 호출하면 해당 클래스의 객체가 생성되지만, `__new__()` 메서드를
오버라이딩 하면 다르게 작동할 수 있다.)
- ### 클래스 객체
  클래스가 `__call__()`메서드를 구현하면 이 클래스의 객체는 함수로 호출될 수 있다.
- ### 제네레이터 함수
  `yield`키워드를 사용하는 함수나 메서드. 이 함수가 호출되면 제네레이터 객체를 반환한다.


파이썬에는 다양한 callable 형이 존재하기 때문에, `callable()` 내장 함수를 사용하여 호출할 수 있는 객체인지
판단하는 방법이 가장 안전하다. 아래의 예시를 확인해보자.
```pycon
>>> abs, str, 13
(<built-in function abs>, <class 'str'>, 13)

>>> [callable(obj) for obj in (abs, str, 13)]
[True, True, False]
```
abs는 내장 함수, str은 클래스로써 callable형이며, 13은 callable형이 아니다.  
이를 확인하기 위해 `callable()` 내장 함수를 이용하면, 실제로 `["True", "True", "False"]` 가 출력됨을 확인할 수 있다.

## 사용자 정의 callable형
파이썬 함수가 실제 객체일 뿐만 아니라, 모든 파이썬 객체가 함수처럼 동작하게 만들 수 있다.  
`__call__()` 인스턴스 메소드를 구현하면 모든 파이썬 객체를 함수처럼 동작하게 만들 수 있다.  

```python
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
```
```pycon
>>> bingo = BingoCage(range(3))
>>> bingo.pick()
2
>>> bingo()
0
>>> callable(bingo)
True
```
BingoCage의 경우 객체를 함수처럼 호출할 때마다 항목을 하나 꺼낸 후 변경된 상태를 유지해야 하는데, `__call__()`메서드를 구현하면 이런 객체를 생성하기 쉽다.  
이런 예로는 decorator가 있다. decorator는 함수이지만, 때때로 호출된 후의 상태를 기억할 수 있는 기능이 유용하게 사용된다.  

## 함수 인트로스펙션
함수 객체는 `__doc__`이외에도 많은 속성을 가지고 있다. 일반적인 객체에는 없지만 함수에는 있는 고유한 속성을 알아보자.  
집합으로 변환한 뒤, 차집합을 구하는 방식으로 객체에는 없지만 함수에는 있는 고유한 속성을 나타내보았다. 
```pycon
>>> class C: pass
>>> obj = C()
>>> def func(): pass
>>> sorted(set(dir(func)) - set(dir(obj)))
['__annotations__', '__call__', '__closure__', '__code__', '__defaults__', '__get__', '__globals__', '__kwdefaults__', '__name__', '__qualname__']
```

## 함수 매개변수에 대한 정보
함수에 어떤 매개변수가 필요한지, 매개변수에 기본값이 있는지 없는지 확인할 수 있는 방법은 무엇이 있을까?  
함수 객체 안의 `__defaults__`속성에는 위치 인수와 키워드 인수의 기본값을 가진 튜플이 들어있다.  
키워드 전용 인수의 기본값은 `__kwdefaults__`속성에 들어 있다. 그러나 인수명은 `__code__`속성에 들어 있는데,  
이 속성은 여러 속성을 담고 있는 code 객체를 가리킨다.  
예제와 함께 알아보자

