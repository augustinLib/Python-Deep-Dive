# function(함수)

## 목차
[1. parameter(매개변수)](#parameter(매개변수))  
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










