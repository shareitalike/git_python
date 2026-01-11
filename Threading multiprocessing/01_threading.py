import threading
import time
#time.sleep() simulates waiting
#CPU is mostly idle
#Threads overlap waiting time
#That’s why threading works beautifully here.
#Threading doesn’t make Python faster — it makes waiting smarter.

def take_orders():
    for i in range(1, 4):
        print(f"Taking order for #{i}")
        time.sleep(2)

def brew_chai():
    for i in range(1, 4):
        print(f"Brewing chai for #{i}")
        time.sleep(3)
        
# create threads
order_thread = threading.Thread(target=take_orders)
brew_thread = threading.Thread(target=brew_chai)
#Multithreading, Never assume print order in threading
#OS scheduler decides which thread runs next
order_thread.start()
brew_thread.start()

# wait for both to finish
order_thread.join()
brew_thread.join()
#if join is not done then below print executes after first order , then
# other order gets executes  after wait tome finishes
print(f"All orders taken and chai brewed")


