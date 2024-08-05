# Parallize

Parallize is a Python package that provides utilities to parallelize synchronous functions using the `concurrent.futures.ProcessPoolExecutor` and convert it into async functions to prevent the main thread from blocking. This allows you to execute functions in separate processes, leveraging multiple CPU cores for improved performance.

## Features

- **Parallelize Synchronous Functions**: Execute synchronous functions in parallel using multiple processes.
- **Parallelize Asynchronous Functions**: Execute asynchronous functions in parallel using multiple processes.
- **Customizable Worker Count**: Specify the maximum number of worker processes to use, or let the package use the number of available CPU cores by default.

## Mini Benchmark

Here are the updated benchmark results comparing serial and parallel execution times using the `test_aparallize.py` test case:

| Test Case            | Concurrent Execution Time | Parallel Execution Time | Speedup | Tasks Count |
| -------------------- | ------------------------- | ----------------------- | ------- | ----------- |
| `test_aparallize_fn` | 0:00:17.215937            | 0:00:08.293026          | 2.08x   | 2           |
| `test_aparallize_10` | 0:01:25.070893            | 0:00:13.997451          | 5.94x   | 10          |

### Benchmark Details

- **Concurrent Execution Time**: The time taken to execute the CPU-bound task concurrently using a `ThreadPoolExecutor`.
- **Parallel Execution Time**: The time taken to execute the same task in parallel using the `aparallize` decorator.
- **Speedup**: The ratio of serial execution time to parallel execution time, indicating the performance improvement achieved by parallelizing the task.

## Installation

To install Parallize, you can use pip:

```bash
pip install parallize
```

## Usage

```python
from parallize import aparallize

def my_function(x, y):
    return x + y

# Call the function as usual
result = await aparallize(my_function)(1, 2)
print(result)  # This will be executed in a separate process
```

### Customizing the Number of Workers

You can specify the maximum number of worker processes to use by passing the `max_workers` argument to the decorator:

```python
def my_function(x, y):
    return x + y

result = await aparallize(my_function, max_workers=4)(1, 2)
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
