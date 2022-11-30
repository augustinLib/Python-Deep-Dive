# inner function
def outer(name):
    def inner():
        print("Hello ", name)
    return inner


func = outer("Lee")
# func()


def hello(name, age, gender):
    def inner():
        print(name, ", hello!")
        print("age :", age)
        print("gender :", gender)

    return inner

closure = hello("Lee", 25, "male")
closure()

print(dir(closure))
print(type(closure.__closure__))
print(closure.__closure__)
print(dir(closure.__closure__[0]))
print(closure.__closure__[0].cell_contents)

for i in closure.__closure__:
    print(i.cell_contents)