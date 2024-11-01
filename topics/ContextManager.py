from datetime import datetime
from contextlib import contextmanager
import os

# =============== Creating context manager using class methods ===============


class OpenFile():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()
        os.remove(self.filename)  # delete test file


with OpenFile('sample.txt', 'w') as f:
    text = "Testing cm with class"
    print(text)
    f.write(text)
print("File is closed" if f.closed else "File is still opened")
print("---------------------------------------------------------------")

# =============== Creating context manager using decorated function ===============


@contextmanager
def open_file(file, mode):
    try:
        f = open(file, mode)
        yield f
    finally:
        f.close()
        os.remove(file)  # delete test file


with open_file('sample.txt', 'w') as f:
    text = "Testing cm with decorated function"
    print(text)
    f.write(text)
print("File is closed" if f.closed else "File is still opened")
print("---------------------------------------------------------------")

# # Another example

# @contextmanager
# def simple_cm(obj):
#     try:
#         obj.some_property += 1
#         yield
#     finally:
#         obj.some_property -= 1

# =============== Creating log file using context manager ===============


HEADER = f'{datetime.now()}\n'
FOOTER = '\n------------------------\n'


@contextmanager
def open_log(file):
    try:
        f = open(file, 'a')
        f.write(HEADER)
        yield f
    finally:
        f.write(FOOTER)
        f.close()


for i in range(1, 11):
    with open_log('log.txt') as log:
        log.write(f'\nRecord number {i}\n')
