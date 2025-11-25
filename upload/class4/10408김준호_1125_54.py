X = 3
Y = 5

def F( A, B):
    A=A+3
    B=A+B
    return A,B

X,Y = F(X,Y)
print(X + Y)
print(X)
print(Y)
