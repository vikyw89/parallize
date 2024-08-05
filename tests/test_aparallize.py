import asyncio
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import pytest
from parallize import aparallize


def cpuboundtask(rn: int = 10**6) -> int:
    # Simulate a CPU-bound task by performing some calculations
    for _ in range(200):
        result = sum(i * i for i in range(rn))
    return result


@pytest.mark.asyncio
async def test_aparallize_fn():
    start_time = datetime.now()

    # Concurrent execution
    with ThreadPoolExecutor() as executor:
        coros = [executor.submit(cpuboundtask, rn=10**6) for _ in range(2)]
        result = [c.result() for c in coros]

    end_time = datetime.now()
    without_parallize = end_time - start_time

    print(f"Serial execution time: {without_parallize}")
    print(f"Result: {result}")

    start_time = datetime.now()

    # Parallel execution
    coros = [aparallize(cpuboundtask)(rn=10**6) for _ in range(2)]
    parallized_result = await asyncio.gather(*coros)

    end_time = datetime.now()
    with_parallize = end_time - start_time

    print(f"Parallel execution time: {with_parallize}")
    print(f"Parallized Result: {parallized_result}")

    assert result == parallized_result
    assert without_parallize.total_seconds() > with_parallize.total_seconds()


@pytest.mark.asyncio
async def test_aparallize_10():
    start_time = datetime.now()

    # Concurrent execution
    with ThreadPoolExecutor() as executor:
        coros = [executor.submit(cpuboundtask, rn=10**6) for _ in range(10)]
        result = [c.result() for c in coros]

    end_time = datetime.now()
    without_parallize = end_time - start_time

    print(f"Serial execution time: {without_parallize}")
    print(f"Result: {result}")

    start_time = datetime.now()

    # Parallel execution
    coros = [aparallize(cpuboundtask)(rn=10**6) for _ in range(10)]
    parallized_result = await asyncio.gather(*coros)

    end_time = datetime.now()
    with_parallize = end_time - start_time

    print(f"Parallel execution time: {with_parallize}")
    print(f"Parallized Result: {parallized_result}")

    assert result == parallized_result
    assert without_parallize.total_seconds() > with_parallize.total_seconds()
