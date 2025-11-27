x = 3
y = 5

def F():
    global x,y
    x = x + 3
    y = x + y
    print(x + y)

F()
print(x)
print(y)
  
