# 클로저(Closure)
## 내부 함수
내부 함수란, 함수 안에서 정의되는 함수이다
예제를 통해 살펴보도록 하겠다.
```python
def outer(name):
    def inner():
        print("Hello ", name)
    return inner


func = outer("Lee")
func() # >>> Hello  Lee
```
예제를 실행시키면, 먼저 `func = outer("Lee")`에서 `outer`함수가 실행된다.  
이후, `outer`함수의 parameter인 `name`에 "Lee"이 할당되게 된다. 이 때, name은 **외부 함수 `outer`에서 사용하는 지역 변수이다.**  
그 다음 내부 함수 `inner`가 정의되고, 이 내부 함수 `inner`를 반환하게 된다.  
그렇다면,  `func = outer("Lee")` 표현식에서 변수 `func`에는 어떤 것이 할당되어질까? 바로, `outer`함수의 return값인 `inner`함수이다.  
**즉, 변수 `func`는 내부 함수 `inner`를 가리키는 것이다.**  
이후 호출 연산자`()`와 함께 변수 `func`를 호출하면 내부 함수 `inner`가 호출되어 `print("Hello ", name)`구문이 실행되는 것이다.  
이 과정을 정리하자면 다음과 같다.
1. 표현식 `func = outer("Lee")` 평가됨
2. `outer`함수의 parameter인 `name`에 "Lee"이 할당
3. 내부 함수 `inner`가 정의됨
4. 내부 함수 `inner`를 반환
5. 변수 `func`에 `outer`함수의 return값인 `inner`함수 할당됨   
   -> **변수 `func`는 내부 함수 `inner`를 가리킴**  
6. 호출 연산자`()`와 함께 변수 `func`를 호출
7. 내부 함수 `inner`가 호출되어 `print("Hello ", name)`구문이 실행


그런데, `outer`함수는 표현식 `func = outer("Lee")` 평가되어 실행될 때 이미 종료되었지만, 이후 내부 함수 `inner`가 호출 될 때
`outer`함수가 가지고 있는 자원을 가지고 실행됨을 확인할 수 있다.  
어떻게 이러한 현상이 발생할 수 있을까? 아래의 클로저(Closure) 항목에서 자세히 살펴보도록 하겠다.

## 클로저(Closure)
클로저(Closure)는, 함수가 종료되어도 자원을 사용할 수 있는 함수이다.
클로저가 되는 3가지 조건은 다음과 같다.
- 내부 함수여야만 한다
- 외부 함수의 변수를 참조해야 한다
- 외부 함수가 내부 함수를 반환해야 한다
위의 3가지의 조건을 만족해야지만 클로저가 될 수 있다.   

위의 예제에서의 `inner`함수는 이 조건을 만족한다. 하나씩 살펴보자면,
- 내부 함수여야만 한다  
  **= `outer`함수 안에 정의된 내부 함수이기 때문에 조건 만족**
- 외부 함수의 변수를 참조해야 한다  
  **= `name`이라는 외부 함수 `outer`의 변수를 참조하기 때문에 조건 만족**
- 외부 함수가 내부 함수를 반환해야 한다  
  **= `return inner`구문으로 외부 함수 `outer`가 내부 함수 `inner`를 반환하기에 조건 만족**

따라서, 함수 `inner`는 클로저(Closure)이며, 외부 함수 `outer`가 종료되어도 `outer`함수가 가지고 있는 자원을 가지고 실행될 수 있는 것이다.  

그렇다면, 외부 함수의 변수를 참조한 (예제에서는 `name`) 그 변수는 어디에 저장되는 것일까?  
추가적인 예제와 함께 알아보도록 하겠다.  
```python
def hello(name, age, gender):
    def inner():
        print(name, ", hello!")
        print("age :", age)
        print("gender :", gender)

    return inner

closure = hello("Lee", 25, "male")
closure()
```
위의 예제와 마찬가지로 이 예제의 실행 과정을 차근차근 살펴보겠다.  
1. 표현식 `closure = hello("Lee", 25, "male")` 평가됨
2. `hello`함수의 parameter인 `name`, `age`, `gender`에 "Lee", 25, "male"이 할당
3. 내부 함수 `inner`가 정의됨
4. 내부 함수 `inner`를 반환
5. 변수 `closure`에 `hello`함수의 return값인 `inner`함수 할당됨   
   -> **변수 `closure`는 내부 함수 `inner`를 가리킴**  
6. 호출 연산자`()`와 함께 변수 `closure`를 호출
7. 내부 함수 `inner`가 호출되어 `inner`함수의 내부 구문이 실행

이러한 과정을 거쳐 다음과 같은 결과가 출력된다
```
Lee , hello!
age : 25
gender : male
```
위의 예제에서의 `inner`함수 또한 클로저(Closure)가 되는 3가지 조건을 만족한다. 하나씩 살펴보자면,
- 내부 함수여야만 한다  
  **= `hello`함수 안에 정의된 내부 함수이기 때문에 조건 만족**
- 외부 함수의 변수를 참조해야 한다  
  **= `name`, `age`, `gender`의 외부 함수 `hello`의 변수를 참조하기 때문에 조건 만족**
- 외부 함수가 내부 함수를 반환해야 한다  
  **= `return inner`구문으로 외부 함수 `hello`가 내부 함수 `inner`를 반환하기에 조건 만족**

따라서, 함수 `inner`는 클로저(Closure)이며, 외부 함수 `hello`가 종료되어도 `hello`함수가 가지고 있는 자원을 가지고 실행될 수 있다.  
이제, 함수 `inner`에서 외부 함수 `hello`의 변수를 참조한 변수들(`name`, `age`, `gender`)이 어디에 저장되는지 알아보도록 하겠다.  
먼저, `closure`이라는 변수, 즉 클로저(Closure) 객체 내부를 `dir()`함수로 살펴보도록 하겠다.  
```pycon
>>> print(dir(closure))
['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
```
클로저(Closure) 객체 내부에 있는 메소드 중 `__closure__`이라는 메소드를 확인할 수 있다.  
`__closure__` 메소드를 실행하면 반환되는 값과, 해당 값의 type을 알아보자.
```pycon
>>> print(closure.__closure__)
(<cell at 0x101de2700: int object at 0x1000f2c30>, <cell at 0x101de29a0: str object at 0x101e09770>, <cell at 0x101dfea30: str object at 0x101e099f0>)
>>> print(type(closure.__closure__))
<class 'tuple'>
```
`__closure__` 메소드를 실행하면, tuple을 반환하는 것을 확인할 수 있다.  
tuple 안에는 `<cell at 0x101de2700: int object at 0x1000f2c30>`와 같은 object들이 있는 것을 확인할 수 있는데, 우리는 위 예제에서
int형 변수 1개, str형 변수 2개를 참조했기 때문에 각 tuple의 값에 int object 1개, str object 2개가 있는 것을 확인할 수 있다.  
이러한 각각의 요소들도 또 object이기 때문에, 다시 한번 `dir()`함수로 내부를 살펴보겠다.
```pycon
>>> print(dir(closure.__closure__[0]))
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'cell_contents']
```
튜플의 첫 번째 요소인  `<cell at 0x101de2700: int object at 0x1000f2c30>` 객체에 `dir()`함수로 메소드를 살펴보았다.  
여러 메소드들 중에서, `cell_contents`라는 메소드가 보일 것이다.  
이 메소드를 통해서, 해당 객체가 담고있는 contents를 확인할 수 있는데, 직접 확인해보도록 하겠다.
```pycon
>>> print(closure.__closure__[0].cell_contents)
25
```
위 예제에서 외부 함수 `hello()`에 인자로 넘겨준 25가 담겨있음을 확인할 수 있다.  
이 과정을 통해 우리가 알 수 있는 것은 다음과 같다.
>  **클로저(Closure) 객체 안에는 외부 함수의 데이터를 담고 있는 공간이 있으며,**  
> 이는 `<클로저(Closure) 객체>.__closure__[<index>].cell_contents`로 조회 가능하다.

그렇다면, 이러한 클로저(Closure)는 언제 사용될까?  
사실, 클로저(Closure)는 전역 변수를 사용함으로써 대체가 가능하다. 우리가 살펴봤던 예제도 결국 예제 코드 위에 
전역 변수를 선언하고, 해당 전역 변수를 함수의 인자로 넘겨주면 굳이 클로저를 사용하지 않고도 같은 결과를 얻을 수 있다.  
그러나, 전역 변수는 naming이 겹치거나, scope가 겹치는 등의 문제를 발생시킬 수 있다.  

>**따라서, 우리는 클로저(Closure)를 이용함으로써 함수마다의 scope 안에 변수들을 저장함으로 전역 변수를 사용하는 문제를 해결할 수 있다.**  

또한, generator와 decorator를 이해하는데 필수적인 요소이기 때문에 보다 클로저(Closure)와 친숙해질 필요가 있다.  


# Decorator
데코레이터(Decorator)는 다른 함수를 인수로 받는 callable이다.  
이러한 데코레이터(Decorator)는 함수의 앞, 뒤(함수가 실행되기 이전, 함수가 실행된 이후)로 부가적인 기능을 넣어주고 싶을 때 사용된다.  
이 때, 앞과 뒤, 모두 넣지 않고 앞에만 부가적인 기능을 넣어줄 수 있고, 마찬가지로 뒤에만 부가적인 기능을 넣어줄 수 있다.  
그런데, 꼭 데코레이터(Decorator)를 사용하여 함수의 앞, 뒤(함수가 실행되기 이전, 함수가 실행된 이후)에 부가적인 기능을 넣어줘야 할까?
예제와 함께 살펴보도록 하겠다.
```python
def say_hello():
    print("Hello user!")

def say_bye():
    print("Bye user!")
```
다음과 같이 hello와 bye를 출력하는 함수가 있다고 가정해보자.  
만약 함수의 앞,뒤로 함수가 시작되었고, 함수가 끝났다는 로그를 출력하려면 간단하게는 다음과 같이 함수 내부를 바꿔주는 방법이 있다.  
```python
def say_hello():
    print("function start")
    print("Hello user!")
    print("function end")

def say_bye():
    print("function start")
    print("Bye user!")
    print("function end")
```
그러나, 만약 우리가 위와 같은 방법으로 함수의 시작과 끝을 알려주는 로그 출력 기능을 많은 함수에 적용하려면 일일히 함수의 내용을 바꿔줘야 하는 번거로움이 발생한다.  
또한, 같은 부분(`print("function start")`, `print("function end")`)이 중복되는 문제도 발생한다.  

**우리의 데코레이터(Decorator)는 이러한 함수 내부에서의 반복을 제거해주는 역할을 한다.**  
데코레이터(Decorator)를 사용하는 방법은 크게 두 단계로 나뉜다.
1. 클로저(Closure)를 이용하여 데코레이터(Decorator)생성
2. 데코레이터(Decorator)를 적용하고 싶은 함수 앞에 `@데코레이터(Decorator)` 입력

이 또한 예제와 함께 살펴보도록 하겠다.  
```python
def logger(func):
    def wrapper(arg):
        print("function start")
        func(arg)
        print("function end")

    return wrapper


@logger
def say_hello(name):
    print("Hello", name)


@logger
def say_bye(name):
    print("Bye", name)
```
위 예제를 실행하면 위에서 함수 내부를 수정한것과 같은 결과가 나온다
```pycon
>>> say_hello("Lee")
function start
Hello Lee
function end

>> say_bye("Lee")
function start
Hello Lee
function end
```
그렇다면, 예제를 실행시키면 어떤 과정을 거쳐서 결과가 출력될까?  
먼저, `@logger`라는 데코레이터(Decorator)가 지정이 되어있으면, 해당 데코레이터(Decorator)를 찾게 된다.  
이후, 데코레이터(Decorator)가 적용된 함수를 데코레이터(Decorator)의 인자(parameter)로 넘겨준다.  

1. `say_hello()`함수 실행
2. `@logger`라는 데코레이터(Decorator)가 지정되어있음을 확인
3. `@logger`라는 데코레이터(Decorator) 탐색
4. 데코레이터(Decorator)가 적용된 `say_hello()` 함수를 데코레이터(Decorator)의 인자(parameter)로 넘겨준다.
5. 



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