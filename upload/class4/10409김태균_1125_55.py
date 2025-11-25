X = 3
Y = 5

def F():
    global X, Y
    X = X + 3
    Y = X + Y
    print(X + Y)

F()
print(X)
print(Y)
