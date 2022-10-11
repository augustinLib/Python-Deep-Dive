# filter(함수, 순서가 있는 자료형)
def func(x):
    return x < 0


# return : filter object


filter(func, [-3, -2, 0, 5, 7])
