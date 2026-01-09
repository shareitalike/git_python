
def printer():
    while True:
        item = yield
        print("Consumed:", item)

def uppercase(next_stage):
    while True:
        item = yield
        next_stage.send(item.upper())


def filter_short(next_stage):
    while True:
        item = yield
        if len(item) > 3:
            next_stage.send(item)

printer_gen = printer()
next(printer_gen)

upper_gen = uppercase(printer_gen)
next(upper_gen)

filter_gen = filter_short(upper_gen)
next(filter_gen)

# PRODUCER
filter_gen.send("tea")
filter_gen.send("chai")
filter_gen.send("masala chai")
