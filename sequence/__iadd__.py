list1 = [11, 22, 33, 44, 55]
list2 = [66, 77, 88, 99]

# s.__iadd__(s2)
# s += s2 : 리스트를 연결하고 s에 저장한다

# list
list1.__iadd__(list2)
print(list1)
# -> [11, 22, 33, 44, 55, 66, 77, 88, 99]