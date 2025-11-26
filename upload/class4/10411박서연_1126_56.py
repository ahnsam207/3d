from math import pi

def area_chircle(radius, n):
    area = pi * radius ** 2
    return round(area, n)

print(area_chircle(3, 1))
print(area_chircle(5, 2))
print(area_chircle(9, 3))
