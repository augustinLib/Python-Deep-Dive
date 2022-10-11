# map(함수, 순서가 있는 자료형)
map(int, ["3", "4", "5", "6"])
# return : map object

list(map(int, ["3", "4", "5", "6"]))


# 리스트 각 요소 공백 지우기
def strip_all(x):
    return x.strip()


items = [' el1', ' el2 ']
items = list(map(strip_all, items))
print(items)

# 람다 함수와 함께 활용
items = [' el1', ' el2 ']
items = list(map(lambda x: x.strip(), items))
