coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)

traveler_ids = [("USA", "31195855"), ('BRA', 'CE342567'), ("ESP", "XDA205856")]

for passport in sorted(traveler_ids):
    print("%s/%s" % passport)

for country, _ in sorted(traveler_ids):
    print(country)

# tuple unpacking
a = 10
b = 20

a, b = b, a     # a = 20, b = 10

divmod(20, 8)
