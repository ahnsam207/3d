from math import pi

def area_cirle(radius, n) :
    area = pi * radius ** 2
    return round(radius, n)
print(area_cirle(3, 1))
