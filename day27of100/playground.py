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



print(add(3,5,6,2,5,5,1515,158515))