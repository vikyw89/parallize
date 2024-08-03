from parallize import parallize
from datetime import datetime


def cpuboundtask(rn: int = 10**6) -> int:
    # Simulate a CPU-bound task by performing some calculations
    for _ in range(100):
        result = sum(i * i for i in range(rn))
    return result


@parallize
def cpuboundtask_w_parallize(rn: int = 10**6) -> int:
    # Simulate a CPU-bound task by performing some calculations
    for _ in range(100):
        result = sum(i * i for i in range(rn))
    return result


def test_parallize():
    start_time = datetime.now()

    cpuboundtask(rn=10**6)

    end_time = datetime.now()
    without_parallize = end_time - start_time
    print(f"Serial execution time: {without_parallize}")

    start_time = datetime.now()

    parallize(cpuboundtask)(rn=10**6)

    end_time = datetime.now()
    with_parallize = end_time - start_time
    print(f"Parallel execution time: {with_parallize}")

    assert without_parallize.total_seconds() > with_parallize.total_seconds() * 2


def test_parallize_decorator():
    start_time = datetime.now()

    cpuboundtask(rn=10**6)

    end_time = datetime.now()
    without_parallize = end_time - start_time
    print(f"Serial execution time: {without_parallize}")

    start_time = datetime.now()

    cpuboundtask_w_parallize(rn=10**6)

    end_time = datetime.now()
    with_parallize = end_time - start_time
    print(f"Parallel execution time: {with_parallize}")

    assert without_parallize.total_seconds() > with_parallize.total_seconds() * 2
