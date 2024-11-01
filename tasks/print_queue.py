import random


class PrintQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []


class Job:
    def __init__(self):
        self.pages = random.randint(1, 11)

    def print_page(self):
        if self.pages > 0:
            self.pages -= 1

    def check_complete(self):
        if self.pages == 0:
            return True
        return False


class Printer:

    def __init__(self):
        self.current_job = None

    def get_job(self, print_queue):
        try:
            self.current_job = print_queue.dequeue()
        except IndexError:      # queue is empty
            return "No more jobs to print"

    def print_job(self):
        job = self.current_job
        if job is None:
            return "No job to print."
        while job.pages > 0:
            job.print_page()
        if job.check_complete():
            return "Printing complete."
