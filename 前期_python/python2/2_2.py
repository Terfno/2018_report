def f():
    global x
    print(x)
    x=1
x=100
f()
print(x)
