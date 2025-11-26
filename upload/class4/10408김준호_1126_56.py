from math import pi

def area_circke(radius, n) :
    area = pi * radius ** 2
    return round(area, n)

print(area_circle(3, 1))
print(area_circle(5, 2))
print(area_circle(7, 3))
