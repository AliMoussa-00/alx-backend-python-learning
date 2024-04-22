# Asynchronous Programming with Python: Understanding Coroutines and asyncio

[tasks](https://drive.google.com/file/d/1_ztzkpWDRZd8rp-vVEl7v1dS_juGi085/view?usp=drive_link)

---

## Introduction

Asynchronous programming in Python offers a powerful way to write concurrent code (handle multiple tasks at once) that is efficient and responsive. Two key components of asynchronous programming in Python are **coroutines** and the **asyncio** module. This README aims to provide a comprehensive understanding of these concepts and how they work together.

## Coroutines

### What are Coroutines?

Coroutines are a special type of function in Python that can pause and resume their execution at specific points. They allow you to write code that can be executed concurrently, making them particularly useful for I/O-bound tasks where waiting for I/O operations to complete is a significant part of the workload.

### Defining Coroutines

In Python, coroutines are defined using the `async` keyword before the `def` statement:

```python
async def my_coroutine():
    # Coroutine logic here
```

### Coroutine Execution

Coroutines are not executed like regular functions. Instead, they are scheduled to run within an `event loop.` The event loop manages the execution of coroutines, **switching between them when they are paused**, typically using the `await` keyword.

## asyncio Module

### What is asyncio?

`asyncio` is a module in Python's standard library that provides a framework for asynchronous programming. It includes features for defining and running coroutines, managing concurrency, and handling I/O operations efficiently.

### Key Components of asyncio

1. **Event Loop**: The event loop is the core of asyncio. It schedules and runs coroutines, handles waiting for I/O operations, and switches between coroutines as needed.
  
2. **Task**: Tasks are used to schedule coroutines for execution within the event loop. They represent units of work that can run concurrently.
  
3. **Future**: Futures represent the result of an asynchronous operation that has not yet completed. They are used to track the status of asynchronous operations and retrieve their results when they are complete.
  

### Using asyncio

To use asyncio, you typically define coroutines using the `async` keyword and execute them within an event loop. Here's a basic example:

```python
import asyncio

async def my_coroutine():
    # Coroutine logic here

async def main():
    await my_coroutine()

asyncio.run(main()) # pass the cotoutines to the event loop and start execution
```

## async/await Syntax

### What are async and await?

`async` and `await` are keywords introduced in Python 3.5 to define and interact with coroutines, respectively. They provide a more concise and readable syntax for asynchronous programming compared to using callbacks or explicit event loop management.

### Using async/await

You use the `async` keyword to define coroutines and the `await` keyword to suspend the execution of a coroutine until an asynchronous operation completes. Here's an example:

```python
async def my_coroutine():
    result = await async_operation()
    # Process the result
```

---

### Running Concurrent Coroutines:

You can run multiple coroutines concurrently using `asyncio.gather()` or by creating tasks with `asyncio.create_task()`.

```python
import asyncio

async def coroutine1():
    print("Coroutine 1")
    await asyncio.sleep(1)
    print("Coroutine 1 done")

async def coroutine2():
    print("Coroutine 2")
    await asyncio.sleep(2)
    print("Coroutine 2 done")

async def main():
    await asyncio.gather(coroutine1(), coroutine2())

asyncio.run(main())

```

---

## Using `asyncio.gather()`

`asyncio.gather()` is a convenient way to concurrently execute multiple coroutines and collect their results. It takes multiple awaitable objects (such as coroutines) as arguments and runs them concurrently within the event loop.

```python
import asyncio

async def coroutine1():
    await asyncio.sleep(1)
    return "Coroutine 1"

async def coroutine2():
    await asyncio.sleep(2)
    return "Coroutine 2"

async def main():
    results = await asyncio.gather(coroutine1(), coroutine2())
    print("Results:", results)

asyncio.run(main())

```

---

## Using `asyncio.as_completed()`

`asyncio.as_completed()` is useful when you want to process the results of coroutines as soon as they become available, without waiting for all of them to complete. It takes an iterable of awaitable objects (such as coroutines) and yields futures as they are completed.

```python
import asyncio

async def coroutine1():
    await asyncio.sleep(1)
    return "Coroutine 1"

async def coroutine2():
    await asyncio.sleep(2)
    return "Coroutine 2"

async def main():
    tasks = [coroutine1(), coroutine2()]
    for future in asyncio.as_completed(tasks):
        result = await future
        print("Result:", result)

asyncio.run(main())

```

---

## Tasks vs Async

Creating a task in asyncio is similar to executing an async function, but with a slight difference in how it's handled.

When you create a task using `asyncio.create_task()`, you're essentially scheduling the execution of an async function (or coroutine) to run concurrently within the asyncio event loop. This allows you to execute the function asynchronously without blocking the main thread of execution.

Here's a breakdown of the similarities and differences:

### Similarities:

1. **Asynchronous Execution**: Both tasks and async functions allow you to execute code asynchronously, meaning they can run concurrently with other tasks or code.
  
2. **Non-Blocking**: Tasks, like async functions, allow you to perform I/O-bound operations without blocking the main thread, leading to improved concurrency and responsiveness.
  

### Differences:

1. **Task Management**: Creating a task explicitly using `asyncio.create_task()` gives you more control over the task's lifecycle, such as cancelling, waiting for, or gathering results from the task.
  
2. **Return Type**: Tasks have a different return type (`asyncio.Task`) compared to async functions, which return awaitable objects directly (e.g., coroutine objects).
  
3. **Concurrency Model**: Tasks are managed by the event loop and can run concurrently with other tasks, whereas async functions are executed sequentially unless you explicitly await them.
  

Overall, while creating a task and executing an async function both allow for asynchronous execution, tasks provide more flexibility and control over the execution and management of the asynchronous code.

---

## Conclusion

Understanding coroutines, asyncio, and the async/await syntax is essential for writing efficient and responsive asynchronous code in Python. By leveraging these concepts, you can build high-performance applications that handle I/O-bound tasks with ease and scale well under heavy loads.

For more information and advanced usage, refer to the official Python documentation on asyncio: [Python asyncio Documentation](https://docs.python.org/3/library/asyncio.html)
