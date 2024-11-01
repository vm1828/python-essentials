from pytest import fixture
from print_queue import PrintQueue, Job, Printer


@fixture()
def print_queue():
    job1 = Job()
    job2 = Job()
    print_queue = PrintQueue()
    print_queue.enqueue(job1)
    print_queue.enqueue(job2)
    yield print_queue


def test_Printer(print_queue):
    assert len(print_queue.items) == 2
    printer = Printer()

    assert printer.current_job is None
    assert printer.print_job() == "No job to print."

    printer.get_job(print_queue)
    assert len(print_queue.items) == 1

    assert printer.current_job is not None
    assert printer.print_job() == "Printing complete."

    printer.get_job(print_queue)
    assert print_queue.items == []
