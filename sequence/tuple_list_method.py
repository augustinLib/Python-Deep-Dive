tuple1 = (1,2,3,4,5)
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

# s.__iadd__(s2)
# s += s2 : 리스트를 연결하고 s에 저장한다

# list
list1.__iadd__(list2)
print(list1)
# -> [11, 22, 33, 44, 55, 66, 77, 88, 99]

# s.append(e)
# 제일 뒤에 요소를 하나 추가한다

# list
list2.append(777)
print(list2)
# -> [66, 77, 88, 99, 777]

# s.clear()
# 모든 항목을 삭제한다

# list
list2.clear()
print(list2)
# -> []

# s.__contains__(e)
# e in s

# list
print(list1.__contains__(22))
# -> True

# s.copy()
# 리스트를 얇게 복사한다 (원본 리스트의 가장 상위의 리스트의 값만 복사, 하위리스트의 값은 참조)

# list
list3 = list1.copy()
list3.append(232)
print(list1, list3)
print(list1 is list3)
# -> [11, 22, 33, 44, 55, 66, 77, 88, 99] [11, 22, 33, 44, 55, 66, 77, 88, 99, 232]
# -> False


# s.__delitem__(p)
# p 위치의 요소를 삭제한다

# list
list3.__delitem__(9)
print(list3)
# -> [11, 22, 33, 44, 55, 66, 77, 88, 99]


# s.extend(it)
# 반복형 it 안에 있는 요소를 추가한다

# list
list1.extend((34,53,21)) # 반복형 it이기 때문에 리스트에 튜플을 인자로 전달 가능
print(list1)
# -> [11, 22, 33, 44, 55, 66, 77, 88, 99, 34, 53, 21]