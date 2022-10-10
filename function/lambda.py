# define lambda
# lambda parameter : result
plus_one = lambda x: x + 1

# call lambda
print((lambda x: x + 1)(2))
print(plus_one(1))

# lambda와 조건문
# lambda로 if statement 사용 시, else statement까지 필수적으로 사용해야함
print((lambda x: True if x > 0 else False)(3))
