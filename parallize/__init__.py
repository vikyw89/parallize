import asyncio
from concurrent.futures import ProcessPoolExecutor
import sys
from typing import (
    Awaitable,
    Callable,
    TypeVar,
)


if sys.version_info >= (3, 10):
    from typing import ParamSpec
else:
    from typing_extensions import ParamSpec


T_Retval = TypeVar("T_Retval")
T_ParamSpec = ParamSpec("T_ParamSpec")
T = TypeVar("T")


def aparallize(
    function: Callable[T_ParamSpec, T_Retval],
    max_workers: int | None = None,
) -> Callable[T_ParamSpec, Awaitable[T_Retval]]:
    """
    Takes a blocking function and creates an async one that receives the same positional and keyword arguments, and that when called, calls the original function in a worker thread using `anyio.to_thread.run_sync()`. Internally, `asyncer.asyncify()` uses the same `anyio.to_thread.run_sync()`, but it supports keyword arguments additional to positional arguments and it adds better support for autocompletion and inline errors for the arguments of the function called and the return value.

    Args:
        function (Callable[T_ParamSpec, T_Retval]): A blocking regular callable (e.g. a function).
        max_workers (int | None, optional): The maximum number of worker threads to use. Defaults to None.

    Returns:
        Callable[T_ParamSpec, Awaitable[T_Retval]]: An async function that takes the same positional and keyword arguments as the original one, that when called runs the same original function in a thread worker and returns the result.
    """

    async def wrapper(
        *args: T_ParamSpec.args, **kwargs: T_ParamSpec.kwargs
    ) -> T_Retval:
        with ProcessPoolExecutor(max_workers=max_workers) as executor:
            process = executor.submit(function, *args, **kwargs)
            loop = asyncio.get_event_loop()
            return await loop.run_in_executor(None, process.result)

    return wrapper
