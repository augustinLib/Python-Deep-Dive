list1 = [11, 22, 33, 44, 55, 66, 77, 88, 99]

# s.copy()
# 리스트를 얇게 복사한다 (원본 리스트의 가장 상위의 리스트의 값만 복사, 하위리스트의 값은 참조)

# list
list3 = list1.copy()
list3.append(232)
print(list1)
# print(list3)
# print(list1 is list3)
# -> [11, 22, 33, 44, 55, 66, 77, 88, 99] [11, 22, 33, 44, 55, 66, 77, 88, 99, 232]
# -> False
