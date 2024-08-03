from datetime import datetime
from parallize import aparallize
import pytest
from utils import TimeLogger


async def acpuboundtask(rn: int = 10**6) -> int:
    # Simulate a CPU-bound task by performing some calculations
    for _ in range(100):
        result = sum(i * i for i in range(rn))
    return result


@aparallize
async def acpuboundtask_w_aparallize(rn: int = 10**6) -> int:
    # Simulate a CPU-bound task by performing some calculations
    for _ in range(100):
        result = sum(i * i for i in range(rn))
    return result


@pytest.mark.asyncio
async def test_aparallize():
    start_time = datetime.now()

    await acpuboundtask(rn=10**6)

    end_time = datetime.now()
    without_parallize = end_time - start_time
    print(f"Serial execution time: {without_parallize}")

    start_time = datetime.now()

    await aparallize(acpuboundtask)(rn=10**6)

    end_time = datetime.now()
    with_parallize = end_time - start_time
    print(f"Parallel execution time: {with_parallize}")

    assert without_parallize.total_seconds() > (with_parallize.total_seconds() * 2)


@pytest.mark.asyncio
async def test_aparallize_decorator():
    start_time = datetime.now()
    await acpuboundtask(rn=10**6)
    end_time = datetime.now()
    without_parallize = end_time - start_time
    print(f"Serial execution time: {without_parallize}")

    start_time = datetime.now()

    await acpuboundtask_w_aparallize(rn=10**6)

    end_time = datetime.now()
    with_parallize = end_time - start_time
    print(f"Parallel execution time: {with_parallize}")

    assert without_parallize.total_seconds() > (with_parallize.total_seconds() * 2)
