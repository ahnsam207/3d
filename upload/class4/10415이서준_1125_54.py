x = 3
y = 5

def f(a,b):
    a = a + 3
    b = a + b
    return a,b
x,y = f(x,y)
print(x + y)
print(x)
print(y)
