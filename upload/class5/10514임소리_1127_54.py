x = 3
y = 5

def F(A, B):
    A = A + 3
    B = A + B
    return A, B

x, y = F(x, y)
print(x + y)
print(x)
print(y)
