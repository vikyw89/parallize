import asyncio
import functools
import sys
from typing import (
    Any,
    Awaitable,
    Callable,
    Coroutine,
    TypeVar,
    Union,
)

if sys.version_info >= (3, 10):
    from typing import ParamSpec
else:
    from typing_extensions import ParamSpec

from concurrent.futures import ProcessPoolExecutor


T_Retval = TypeVar("T_Retval")
T_ParamSpec = ParamSpec("T_ParamSpec")
T = TypeVar("T")


def aparallize(
    async_function: Callable[T_ParamSpec, Coroutine[Any, Any, T_Retval]],
    max_workers: Union[int, None] = None,
) -> Callable[T_ParamSpec, Awaitable[T_Retval]]:
    """
    Creates a parallelized version of the given async function.

    Args:
        async_function (Callable[T_ParamSpec, Coroutine[Any, Any, T_Retval]]): The async function to be parallelized.
        max_workers (Union[int, None], optional): The maximum number of worker processes to use. If None, it will use the number of available CPU cores. Defaults to None.

    Returns:
        Callable[T_ParamSpec, Awaitable[T_Retval]]: A wrapper function that, when called, will execute the original function in a separate process.
    """

    @functools.wraps(async_function)
    async def wrapper(
        *args: T_ParamSpec.args, **kwargs: T_ParamSpec.kwargs
    ) -> T_Retval:
        partial_f = functools.partial(async_function, *args, **kwargs)

        def inner_wrapper(*args: Any, **kwargs: Any):
            return asyncio.run(partial_f(*args, **kwargs))

        with ProcessPoolExecutor(max_workers=max_workers) as executor:
            return executor.submit(inner_wrapper, *args, **kwargs)

    return wrapper


def parallize(
    function: Callable[T_ParamSpec, T_Retval],
    max_workers: Union[int, None] = None,
) -> Callable[T_ParamSpec, T_Retval]:
    """
    A decorator that parallelizes a given function by executing it in a separate process.

    Args:
    function: The function to be parallelized.
    max_workers: The maximum number of worker processes to use. If None, it will use the number of available CPU cores.

    Returns:
    A wrapper function that, when called, will execute the original function in a separate process.
    """

    @functools.wraps(function)
    def wrapper(*args: T_ParamSpec.args, **kwargs: T_ParamSpec.kwargs) -> T_Retval:
        partial_f = functools.partial(function, *args, **kwargs)

        def inner_wrapper(*args: Any, **kwargs: Any):
            return asyncio.run(partial_f(*args, **kwargs))

        with ProcessPoolExecutor(max_workers=max_workers) as executor:
            return executor.submit(inner_wrapper, *args, **kwargs)

    return wrapper
