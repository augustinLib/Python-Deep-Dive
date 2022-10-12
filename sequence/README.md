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
