import array

symbols = "@#$%^&"
genexp1 = tuple(ord(symbol) for symbol in symbols)
genexp2 = array.array('I', (ord(symbol) for symbol in symbols))


print(genexp1, genexp2)


colors = ["red", "yellow"]
sizes = ["S", "M", "L"]

for tshirts in (f"{color} {size}" for color in colors for size in sizes):
    print(tshirts)
