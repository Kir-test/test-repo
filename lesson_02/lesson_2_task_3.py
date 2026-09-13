import math


def square(side):
    area = side * side

    if side != int(side):
        area = math.ceil(area)

    return area


print(square(5))
print(square(2.5))
