def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


def subtract(*args):
    sum = 0
    for n in args:
        sum -= n
    return sum


def calculated(n , **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)




# calculated(2, add=3, multiply=5)
# print(add(3,5,6,2,5,5,1515,158515))


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make="Nissan") # , model="GT-R")
print(my_car.make)
# print(my_car.model)
