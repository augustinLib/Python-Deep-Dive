tuple1 = (1,2,3,4,5)
tuple2 = (6, 7, 8, 9)
list1 = [11, 22, 33, 44, 55]
list2 = [66, 77, 88, 99]



# s.__getitem__(p)
# s[p] : p위치의 요소를 가져온다

# list
print(list1.__getitem__(2)) # -> 33

# tuple
print(tuple1.__getitem__(2)) # -> 3


# s.insert(p, e)
# p 위치에 있는 요소 앞에 e 요소를 삽입한다

# list
list1.insert(0, 0)
print(list1)
# -> [0, 11, 22, 33, 44, 55, 66, 77, 88, 99, 34, 53, 21]
