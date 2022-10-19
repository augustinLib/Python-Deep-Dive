tuple1 = (1, 2, 3, 4, 5)
tuple2 = (6, 7, 8, 9)
list1 = [11, 22, 33, 44, 55]
list2 = [66, 77, 88, 99]

# s.__add__(s2)
# s + s2 : 리스트를 연결한다

# tuple
print(tuple1.__add__(tuple2))
# -> (1, 2, 3, 4, 5, 6, 7, 8, 9)

# list
print(list1.__add__(list2))
# -> [11, 22, 33, 44, 55, 66, 77, 88, 99]