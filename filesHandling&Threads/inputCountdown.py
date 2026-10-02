import time
import threading

def countdown(seconds, stop_event):
    stop_event.wait(0.2)
    for second in range(seconds, 0, -1):
        print(second, end = ", " if second > 1 else "", flush=True)

        # wait is like time.sleep(), but if the set is true, it returns true the timer stops.
        if stop_event.wait(1):   # sleeps up to 1s, but wakes immediately if stopped
            return               # exit the thread early
    print()

def main():
    for i in range(10, 2, -1):

        print(f"get ready for the next level. now you will have {i} seconds for the task.")
        time.sleep(3)

        # A threading.Event is a simple flag shared between threads.
        # It's either "not set" (False) or "set" (True). Think of it as a light switch both threads can see.
        # important - c# events and python events are different.
        stop_event = threading.Event()

        countdown_thread = threading.Thread(target=countdown, args=(i, stop_event))
        countdown_thread.start()

        try:
            num = int(input(f"press {i} before the countdown is done to get to the next level: "))
        except ValueError:
            num = None

        on_time = countdown_thread.is_alive()
        stop_event.set()
        countdown_thread.join()

        if num != i:
            print("\nyour input was wrong. good luck on the next trial.")
            break
        if not on_time:
            print("\nyou didn't send the number on time. good luck on the next trial.")
            break

        print(f"\nwell done, level {i} completed!\n")

    # an interest python for loop property. the code here will run if the for was not terminated by any "break" keyword.
    else:
        print("You beat every level!")

if __name__ == "__main__":
    main()