x = 3
y = 5

def f():
    global x,y
    x = x + 3
    y = x + y
    print(x + y)

f()
print(x)
print(y)
