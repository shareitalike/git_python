

def subgen():
    yield 1
    yield 2

def maingen():
    yield 0
    yield from subgen()
    yield 3

listing = list(maingen())
print(listing)

def sub():
    while True:
        x = yield
        print("Sub received:", x)

def main():
    yield from sub()

g = main()
next(g)
g.send(10)
g.send(20)
