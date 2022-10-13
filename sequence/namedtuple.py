from collections import namedtuple
# namedtuple을 정의할 때는 클래스명과 필드명 리스트, 총 2개의 매개변수가 필요하다.
# 필드명 리스트는 반복형 문자열이나(['name', 'country']), 공백으로 구분된 하나의 문자열('name country')을 이용한다
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))

print(tokyo)

# 필드명을 이용하여 필드에 접근
print(tokyo.population)
print(tokyo.coordinates)

# 위치를 이용하여 필드에 접근
print(tokyo[1])

# _fields는 클래스의 필드명을 담고있는 튜플
print(City._fields)

LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', "IN", 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data)
print(delhi._asdict())

for key, value in delhi._asdict().items():
    print(key + ":", value)
    