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

## 불변 리스트로서의 튜플
튜플은 요솟값을 변경할 수 없는 불변 리스트이다. 이러한 튜플을 불변 리스트로 사용할 때, 튜플과 리스트가
얼마나 비슷한지 알고 있으면 큰 도움이 된다.  
아래는 튜플과 리스트에서 사용할 수 있는 메서드의 종류들이다. 

|            메서드             |  리스트   |  튜플   |                     설명                     |
|:--------------------------:|:------:|:-----:|:------------------------------------------:|
|      `s.__add__(s2)`       |   O    |   O   |             s + s2 : 리스트를 연결한다             |
|      `s.__iadd__(s2)`      |   O    |       |        s += s2 : 리스트를 연결하고 s에 저장한다         |
|       `s.append(e)`        |   O    |       |             제일 뒤에 요소를 하나 추가한다              |
|        `s.clear()`         |   O    |       |                모든 항목을 삭제한다                 |
|    `s.__contains__(e)`     |   O    |   O   |                   e in s                   |
|         `s.copy()`         |   O    |   O   |                리스트를 앝게 복사한다                |
|        `s.count(e)`        |   O    |       |              e가 발생한 횟수를 계산한다               |
|     `s.__delitem__(p)`     |   O    |       |               p 위치의 요소를 삭제한다               |
|       `s.extend(it)`       |   O    |       |           반복형 it 안에 있는 요소를 추가한다            |
|     `s.__getitem__(p)`     |   O    |   O   |           s[p] : p 위치의 요소를 가져온다            |
|    `s.__getnewargs__()`    |        |   O   |        pickle을 이용해서 최적화된 직렬화를 지원한다         |
|        `s.index(e)`        |   O    |   O   |          s 안에서 e가 처음 나타나는 위치를 찾는다          |
|      `s.insert(p, e)`      |   O    |       |         p 위치에 있는 요소 앞에 e 요소를 삽입한다          |
|       `s.__iter__()`       |   O    |   O   |                 반복자를 가져온다                  |
|       `s.__len__()`        |   O    |   O   |            len(s) : 항목 개수를 구한다             |
|       `s.__mul__()`        |   O    |   O   |             s \* n : 문자열을 반복한다             |
|       `s.__imul__()`       |   O    |       |        s \*= n : 문자열을 반복하여 s에 저장한다         |
|       `s.__rmul__()`       |   O    |   O   |           n \* s : 역순 반복 추가 메서드            |
|       `s.__imul__()`       |   O    |       |        s \*= n : 문자열을 반복하여 s에 저장한다         |
|        `s.pop([p])`        |   O    |       |        마지막 항목이나 p 위치의 항목을 제거하고 반환한다        |
|       `s.remove(e)`        |   O    |       |           e 값을 가진 첫 번째 항목을 삭제한다            |
|       `s.reverse()`        |   O    |       |           항목을 역순으로 배치한 후 s에 저장한다           |
|     `s.__reversed__()`     |   O    |       |       마지막에서 첫 번째 항목까지 반복하는 반복자를 반환한다       |
|   `s.__setitem__(p, e)`    |   O    |       |   s[p] = e : e를 p 위치에 저장하고, 기존 항목을 덮어쓴다    |
| `s.sort([key], [reverse])` |   O    |       | 선택적인 키워드 key와 reverse에 따라 항목을 정렬하고 s에 저장한다 |


## 슬라이싱
파이썬에서 제공하는 list, tuple, str, 그리고 모든 시퀀스형은 슬라이싱 연산을 지원한다.

### 슬라이스와 범위 지정시에 마지막 항목이 포함되지 않는 이유
슬라이스와 범위 지정시에 마지막 항목을 포함하지 않는 관례는 인덱스 번호가 0번부터 시작하는 파이썬, C 등의 언어에서 잘 작동한다.  
이러한 관례는 다음과 같은 장점이 있다.
- 세 개의 항목을 생성하는 `range(3)` 이나 `list1[:3]`처럼 중단점만 이용하여 슬라이스나 범위를 지정할 때 길이를 계산하기 쉬움
- 시작점과 중단점을 모두 지정할 때도 길이를 계산하기 쉽다 -> 중단점에서 시작점을 빼면 길이
- 특정 인덱스를 기준으로 겹침 없이 시퀀스를 분할하기 쉽다  
  Ex) `list1[:3], list1[3:]`

### 슬라이스 객체
슬라이싱을 하기 위해 `seq[start:stop:step]` 표현식을 작성할 경우, 이 표현식이 어떻게 평가되는지 알아보자.  

1. `start:stop:step` 표현식은 `slice(start, stop, step)`의 슬라이스 객체가 된다
2. 파이썬은 `seq.__getitem__(slice(start, stop, step))`을 호출한다


## 시퀀스에 +, * 연산자 사용하기
덧셈 및 곱셈 연산자 +. *는 언제나 **객체를 새로 만들고, 피연산자를 변경하지 않는다** (튜플과 같은 불변 시퀀스에도 사용 가능)  
```pycon
>>> list1 = [1, 2, 3]
>>> l * 5
[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> list1
[1, 2, 3]

>>> "abc" * 3
'abcabcabc'
```

## 시퀀스의 복합 할당
+=과 *= 등의 복합 할당 연산자는 첫 번째 피연산자에 따라 매우 다르게 작동한다.  
+= 연산자가 작동하도록 만드는 메서드는 `__iadd__()`이다. (곱셈 복합 할당 의 경우 `__imul__()`)  
만약 `__iadd__()`가 구현되어 있지 않으면 파이썬은 `__add__()`를 대신 호출한다  
아래의 예제와 함께 살펴보자.
```pycon
>>> a += b
```
a가 `__iadd__()`를 구현하면 구현된 메소드가 호출된다. 이때, a가 가변 시퀀스인 경우 a의 값이 변경된다.  
그러나, a가 `__iadd__()`를 구현하지 않는 경우 **a += b 표현식은 a = a + b가 되어 먼저 a + b를 평가하고 객체를 새로 할당한 후 a에 할당한다.**  
> 즉, `__iadd__()` 메서드 구현 여부에 따라 a변수가 가리키는 객체가 바뀔수도 있고 바뀌지 않을 수도 있다.  

예제와 함께 변수가 가리키는 객체가 달라지는지 확인해보자.
```pycon
# list
>>> list1 = [1,2,3]
>>> id(list1)
4400449984

>>> l *= 2
>>> l
[1, 2, 3, 1, 2, 3]
>>> id(l)
4400449984
```
```pycon
# tuple
>>> tuple1 = (1,2,3)
>>> id(tuple1)
4400313984

>>> tuple1 *= 2
>>> tuple1
(1, 2, 3, 1, 2, 3)
>>> id(tuple1)
4400285536
```
가변 시퀀스인 list에는 변수가 가리키는 객체가 달라지지 않았지만,  
불변 리스트인 tuple은 `__imul__()`를 구현하지 않아 **a \*= b 표현식은 a = a \* b가 되어 먼저 a \* b를 평가하고 객체를 새로 할당한 후 a에 할당한다.**  
따라서 변수가 가리키는 객체가 달라짐을 확인할 수 있다.  
이렇게 불변 시퀀스의 경우, 새로운 항목을 추가하는 대신 항목이 추가된 시퀀스 전체를 새로 만들어 타깃 변수에 저장하기 때문에,  
**불변 시퀀스에 반복적으로 연결 연산을 수행하는 것은 비효율적이다**

### 복합 할당 관련 문제
```pycon
>>> t = (1, 2, [30, 40])
>>> t[2] += [50, 60]
```
다음과 같은 예제가 있을 때, 이 코드를 실행하면 어떻게 될까?  
이제까지 배워온 바에 의하면, 튜플은 불변 시퀀스이기 때문에 에러와 함께 불가능할것으로 생각되어진다. 실제로 실행 시 에러가 발생한다.  
그러나, t를 실행해보면 변경되어져 있다.
```pycon
'''
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/code.py", line 90, in runcode
    exec(code, self.locals)
  File "<input>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
'''
>>> t
(1, 2, [30, 40, 50, 60])
```








