# Parallize

Parallize is a Python package that provides utilities to parallelize both synchronous and asynchronous functions using the `concurrent.futures.ProcessPoolExecutor`. This allows you to execute functions in separate processes, leveraging multiple CPU cores for improved performance.

## Features

- **Parallelize Synchronous Functions**: Execute synchronous functions in parallel using multiple processes.
- **Parallelize Asynchronous Functions**: Execute asynchronous functions in parallel using multiple processes.
- **Customizable Worker Count**: Specify the maximum number of worker processes to use, or let the package use the number of available CPU cores by default.

# Parallize

Parallize is a Python package that provides utilities to parallelize both synchronous and asynchronous functions using the `concurrent.futures.ProcessPoolExecutor`. This allows you to execute functions in separate processes, leveraging multiple CPU cores for improved performance.

## Features

- **Parallelize Synchronous Functions**: Execute synchronous functions in parallel using multiple processes.
- **Parallelize Asynchronous Functions**: Execute asynchronous functions in parallel using multiple processes.
- **Customizable Worker Count**: Specify the maximum number of worker processes to use, or let the package use the number of available CPU cores by default.

## Mini benchmark

- parallel are the same function but with @parallize decorator or parallize function
  Here are the benchmark results comparing serial and parallel execution times:

| Test Case                   | Serial Execution Time | Parallel Execution Time | Speedup |
| --------------------------- | --------------------- | ----------------------- | ------- |
| `test_aparallize`           | 0:00:04.073584        | 0:00:00.017007          | 239.5x  |
| `test_aparallize_decorator` | 0:00:04.027461        | 0:00:00.014918          | 269.9x  |
| `test_parallize`            | 0:00:04.057500        | 0:00:00.013410          | 302.6x  |
| `test_parallize_decorator`  | 0:00:04.042075        | 0:00:00.015465          | 261.4x  |

## Installation

To install Parallize, you can use pip:

```bash
pip install parallize
```

## Usage

### Parallelizing Synchronous Functions Using Decorator

To parallelize a synchronous function, use the `parallize` decorator:

```python
from parallize import parallize

@parallize
def my_function(x, y):
    return x + y

# Call the function as usual
result = my_function(1, 2)
print(result)  # This will be executed in a separate process
```

### Parallelizing Asynchronous Functions Using Decorator

To parallelize an asynchronous function, use the `aparallize` decorator:

```python
import asyncio
from parallize import aparallize

@aparallize
async def my_async_function(x, y):
    await asyncio.sleep(1)
    return x + y

# Call the function as usual
result = my_async_function(1, 2)
print(result)  # This will be executed in a separate process
```

## Another usage without decorator

```python
from parallize import parallize

def my_function(x, y):
    return x + y

# Call the function as usual
result = parallize(my_function)(1, 2)
print(result)  # This will be executed in a separate process
```

### Customizing the Number of Workers

You can specify the maximum number of worker processes to use by passing the `max_workers` argument to the decorator:

```python
@parallize(max_workers=4)
def my_function(x, y):
    return x + y

@aparallize(max_workers=4)
async def my_async_function(x, y):
    await asyncio.sleep(1)
    return x + y
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Issues

If you encounter any issues or have suggestions for improvements, please open an issue on the [GitHub repository](https://github.com/vikyw89/parallize/issues).

## Acknowledgments

- Thanks to the Python community for providing powerful tools and libraries for parallel processing.

@vikyw89-20240804
