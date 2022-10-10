# positional parameter
def my_func(a, b):
    print(a, b)


# 인자가 1, 2가 순서대로 a와 b에 넘겨짐을 확인할 수 있다.
my_func(1, 2)


# default parameter
# content 매개변수의 default값 지정
def info(title, content='no contents'):
    print(f'제목 : {title}')
    print(f"내용 : {content}")


# content 인자에 값을 지정하지 않았기 때문에 default값 출력
info("test")


# keyword parameter
def info(title, content):
    print(f'제목 : {title}')
    print(f"내용 : {content}")


# 키워드를 붙여 호출하기 때문에 매개변수의 순서를 지키지 않아도 된다
info(content="None", title="test")


# positional variable length parameter
# 가변 매개변수 = 개수가 정해지지 않은 매개변수
# 매개변수 앞에 *이 붙음을 확인할 수 있다.
def fruits(*args):
    for arg in args:
        print(arg)


# 매개변수들이 tuple로 묶여서 args로 들어가게 됨
fruits('apple', 'orange', 'mango')


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
