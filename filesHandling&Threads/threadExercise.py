import threading
import time

def walk_dog(dog_name):
    time.sleep(8)
    print(f"Walking dog that is called {dog_name}")

def take_out_trash():
    time.sleep(2)
    print("Taking out trash")

def get_mail():
    time.sleep(4)
    print("Getting mail")

# the ',' is only for python to understand that it's a tuple. if there were more arguments, we wouldn't need this comma.
# the ',' is crucial because without it, it's just a string inside a ().
chore1 = threading.Thread(target=walk_dog, args=("messi",))

# this just created the thread. now the thread knows that when it is started, it executes the function in the target argument.

# now the thread will execute the function.
# although we can't put multiple function as target, we can call other function inside the target function.
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

print(f"the number of chores is {threading.active_count()}")
print(f"the chores are: {threading.enumerate()}")

# the main thread needs to wait until chore1, 2, and 3 will terminate.
# fun fact. we could only do chore1.join() and it would do the same thing because anyway the other threads will terminate before chore 1
chore1.join()
chore2.join()
chore3.join()

# print(f"the number of chores is {threading.active_count()}")
# print(f"the chores are: {threading.enumerate()}")
# output:
# the number of chores is 1
# the chores are: [<_MainThread(MainThread, started 1336)>]

# because it only counts the number of threads that are currently running.

print("all chores completed!")