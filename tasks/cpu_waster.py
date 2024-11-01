#!/usr/bin/env python3
"""Threads that waste CPU cycles"""

import os
import threading

# a symple function that wastes CPU cycles forever


def cpu_waster():
    while True:
        pass


# display information about this process
print("\nProcess ID: ", os.getpid())
print("Active threads count: ", threading.active_count())
print(f"Current thread: {threading.enumerate()[-1]}")

print('\nStarting 4 CPU wasters...')
for i in range(4):
    threading.Thread(target=cpu_waster).start()

    # display information about this process
    print(f"\nStarted CPU waster {i+1}")
    print(f"Created thread {threading.enumerate()[-1]}")
    print("Process ID: ", os.getpid())
    print("Active threads count: ", threading.active_count())
