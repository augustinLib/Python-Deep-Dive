# sequence

## 내장 시퀀스
파이썬 표준 라이브러리는 C로 구현된 아래의 시퀀스형을 제공한다
- ### 컨네이너 시퀀스
  - 서로 다른 자료형의 항목들을 담을 수 있다.
  - 객체에 대한 참조를 담고 있으며, 객체는 어떠한 자료형도 담을 수 있다.
  - list, tuple, collections.deque
- ### 균일 시퀀스
  - 단 하나의 자료형만 담을 수 있다.
  - 객체에 대한 참조 대신 자신의 메모리 공간에 각 항목의 값을 직접 담는다.
  - 컨테이너 시퀀스에 비해 메모리를 더 적게 사용한다.
  - str.bytes, bytearray, memoryview, array.array

시퀀스형은 가변성에 따라서 분류할 수도 있다
- ### 가변 시퀀스
  - list, bytearray, array.array, collections.deque, memoryview
  
- ### 불변 시퀀스
  - tuple, str.bytes


## 지능형 리스트와 제네레이터 표현식
리스트의 경우 **지능형 리스트(listcomp)**, 그 외의 시퀀스의 경우 __제네레이터 표현식(genexp)__ 을 사용하면 시퀀스를 간단하게 생성할 수 있다.  
 
### 지능형 리스트(listcomp)
지능형 리스트는 새로운 리스트를 만드는 역할만을 수행하며, 생성된 리스트를 사용하지 않을 거라면 지능형 리스트 구문 사용을 지양하는것이 좋다.
```python
colors = ["red", "yellow"]
sizes = ["S", "M", "L"]

shirts = [(color, size) for color in colors for size in sizes]
print(shirts)
```

### 제네레이터 표현식(genexp)
튜플, 배열 등의 시퀀스형을 초기화할 때 지능형 리스트를 이용할 수 있지만, 다른 생성자에 전달할 리스트를 만들지 않고도 반복자 프로토콜(iterator protocol)을 이용하여 
항목을 하나씩 생성하는 **제네레이터 표현식은 메모리를 더 적게 사용하는 장점이 있다.**  
제네레이터 표현식은 지능형 리스트와 동일한 구문을 사용하지만, 대괄호 대신 괄호를 사용한다.  
```python
import array

symbols = "@#$%^&"
genexp1 = tuple(ord(symbol) for symbol in symbols)
genexp2 = array.array('I', (ord(symbol) for symbol in symbols))


print(genexp1, genexp2)
```
지능형 리스트에서 살펴보았던 예제를 제네레이터 표현식에서도 살펴보자
```python
colors = ["red", "yellow"]
sizes = ["S", "M", "L"]

for shirts in (f"{color} {size}" for color in colors for size in sizes):
    print(shirts)
```
지능형 리스트에서 살펴보았던때와 다르게 **shirts 리스트의 항목들을 메모리 안에 생성하지 않는다.**  
제네레이터 표현식을 사용하면 for 루프에 전달하기 위한 용도로만 사용하는 리스트를 생성하지 않아도 된다.


## 튜플(tuple)
튜플은 불변 리스트로 사용할 수도 있지만, 필드명이 없는 레코드로 사용할 수도 있다.  

## 레코드로서의 튜플
튜플은 레코드를 담고 있다. 튜플의 각 항목은 레코드의 필드 하나를 의미하며, 항목의 위치가 의미를 결정한다.  
아래는 튜플을 레코드로 사용하는 예시 코드이다.

```python
coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)

traveler_ids = [("USA", "31195855"), ('BRA', 'CE342567'), ("ESP", "XDA205856")]

for passport in sorted(traveler_ids):
    print("%s/%s" % passport)

for country, _ in sorted(traveler_ids):
    print(country)
```

### 튜플 언패킹
위의 예제에서, 2번째 줄에서는 하나의 문장에서 5개 변수에 각각 값을 할당했다.  
또한 3번째 예시에서는 % 연산자는 print()함수의 인수로 전달한 포맷 문자열의 각 슬롯에 passport 튜플의 각 항목을 할당해주었다.  
위 두 가지 예시는 **튜플 언패킹(tuple unpacking)**의 방법을 잘 보여준다.

튜플 언패킹을 이용하면, 다음과 같이 임시 변수를 사용하지 않고도 두 변수의 값을 서로 교환할 수 있다.
```python
a = 10
b = 20

a, b = b, a     # a = 20, b = 10
```
또한, 함수를 호출할 때 인수 앞에 *를 붙여 튜플을 언패킹할 수 있다.
```pycon
>>> divmod(20, 8) # 두 수를 인수로 받아 몫과 나머지를 반환하는 함수
(2, 4)

>>> t = (20, 8)
>>> divmod(t)     # 에러 발생
'TypeError: divmod expected 2 arguments, got 1'

>>> divmod(*t)    # 인수 앞에 *를 붙여 튜플을 언패킹, 두 수를 인자로 전달하게 됨
(2, 4)

>>> quotient, remainder = divmod(*t)    # 인수 앞에 *를 붙여 튜플을 언패킹, 두 수를 인자로 전달하게 됨
>>> quotient, remainder
(2, 4)
```
병렬 할당 시 초과 항목을 *를 통해 가져올 수 있다. 이때, *는 단 하나의 변수에만 적용할 수 있다.
```pycon
>>> a, b, *rest = range(5)
>>> a, b, rest
(0, 1, [2, 3, 4])

>>> a, b, *rest = range(3)
>>> a, b, rest
(0, 1, [2])

>>> a, b, *rest = range(2)
>>> a, b, rest
(0, 1, [])
```

### 내포된 튜플 언패킹
언패킹할 표현식을 받는 튜플은 (a, b, (c, d))처럼 다른 튜플을 내포할 수 있으며, 파이썬은 표현식이 내포된 구조체에 일치하면 처리한다.



### 명명된 튜플(namedtuple)
튜플은 매우 편리하지만, 필드에 이름을 붙일 수 없다는 한계점이 있다. 이러한 한계를 극복하기 위해 namedtuple() 함수가 고안되었다.  
collections.namedtuple() 함수는 필드명과 클래스명을 추가한 튜플의 서브클래스를 생성하는 팩토리 함수이다.  
```python
from collections import namedtuple
# namedtuple을 정의할 때는 클래스명과 필드명 리스트, 총 2개의 매개변수가 필요하다.
# 필드명 리스트는 반복형 문자열이나(['name', 'country']), 공백으로 구분된 하나의 문자열('name country')을 이용한다
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))

print(tokyo)

# 필드명을 이용하여 필드에 접근
print(tokyo.population)
print(tokyo.coordinates)

# 위치를 이용하여 필드에 접근
print(tokyo[1])
```