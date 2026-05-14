# Async Guide

This guide explains Python async programming clearly and directly. It covers the core concepts, how async works, and how it differs from multithreading.

## What is asynchronous programming?

Asynchronous programming lets your code wait for slow operations **without blocking the whole program**.

Instead of sitting idle while waiting for things like network requests, database queries, file operations, or timers, Python can switch to other work.

In Python, async code can pause at `await`, give control back to the event loop, and continue later when the result is ready.

---

## What is `asyncio`?

`asyncio` is Python's built-in library for writing **concurrent code** using the `async` and `await` syntax.

It provides the core tools needed for async programming, such as:

- Event loops
- Coroutines
- Tasks
- Scheduling concurrent operations

Almost everything in Python async programming is built on top of `asyncio`.

`asyncio` is the foundation for many Python async frameworks and tools, including:

- High-performance web servers
- Network applications
- Database connection libraries
- Distributed task systems
- Real-time applications

`asyncio` is especially useful for **I/O-bound tasks** and high-level network programming where your code spends a lot of time waiting for external operations.

---

## Why async is useful

- Keeps programs responsive during slow operations.
- Best for **I/O-bound tasks** like API calls, databases, file access, and timers.
- Makes better use of the thread instead of letting it sit idle while waiting.

---

# Core async concepts

## Coroutine

A coroutine is a special function created using `async def`.

Unlike a normal function, calling it does **not run it immediately**. It creates a coroutine object that can **pause and resume execution**.

A coroutine only runs when the **event loop schedules it**.

Example:

```python
import asyncio

async def task():
    await asyncio.sleep(1)
    return "done"
```

Calling it:

```python
task()
```

This creates a coroutine object, but it does not run yet.

---

## `await`

`await` pauses the current coroutine until another async operation finishes.

While it waits, the event loop can run other tasks instead of blocking the thread.

Example:

```python
result = await task()
```

Flow:

```text
Coroutine starts
       ↓
Hits await
       ↓
Coroutine pauses
       ↓
Event loop runs other tasks
       ↓
Result becomes ready
       ↓
Coroutine resumes
```

Without `await` (or scheduling it as a task), the coroutine is only created and will not run.

---

## Event loop

The event loop is the heart of async programming.

Think of it like a **scheduler** or **traffic controller**.

It decides:

- which coroutine runs now
- which coroutine should pause
- which coroutine should resume

In Python:

```python
asyncio.run(main())
```

This:

1. Creates the event loop
2. Runs the main coroutine
3. Closes the loop when done

Example:

```python
import asyncio

async def main():
    print("Running")

asyncio.run(main())
```

---

## Task

A task is a coroutine scheduled to run by the event loop.

It allows a coroutine to run in the background while other tasks continue.

Example:

```python
task = asyncio.create_task(fetch_data())
```

This tells the event loop to start running the coroutine.

---

## Blocking vs non-blocking

### Blocking

```python
import time

time.sleep(3)
```

- Blocks the entire thread.
- Nothing else can run.

### Non-blocking

```python
await asyncio.sleep(3)
```

- Pauses only the current coroutine.
- The event loop can run other tasks.

---

# How concurrency works in async

Async uses **cooperative concurrency**.

This means coroutines voluntarily give up control when they hit `await`.

That allows one coroutine to wait while others continue running.

Example:

If three tasks are waiting for network responses, the event loop can switch between them instead of waiting for one to finish completely before starting the next.

---

## Running multiple tasks together

`asyncio.gather()` runs multiple coroutines concurrently and waits for all of them to finish.

Example:

```python
results = await asyncio.gather(
    task1(),
    task2(),
    task3(),
)
```

All tasks start immediately and wait at the same time.

### Without `gather()`

```text
Task1 → wait 2 sec
Task2 → wait 2 sec
Task3 → wait 2 sec

Total = 6 sec
```

### With `gather()`

```text
Task1 starts
Task2 starts
Task3 starts

All wait together

Total = 2 sec
```

The total time becomes closer to the **longest task**, not the sum of all task times.

---

# Async vs multithreading

## Async

- Runs on **one thread** with **one event loop**.
- Many tasks work together by **pausing at `await` and continuing later**.
- Best for **I/O tasks** like API calls, database queries, file reading, and network requests.
- Uses **less memory** and has **less overhead** than threads.
- Easier to manage shared data because everything runs in one thread.
- When one task waits for I/O, the event loop quickly runs another task, so **the thread does not sit idle waiting**.

## Multithreading

- Uses **multiple threads** inside one program.
- The **operating system** switches between threads.
- Each thread can work or wait independently.
- Useful for **I/O tasks**, especially when using normal blocking code.
- Threads use **more memory** and have **more overhead** than async.
- Threads share memory, which can cause issues like **race conditions** if multiple threads change the same data.

---

## The main difference

With async, tasks switch only when they reach `await`.

With multithreading, the operating system can switch threads at any time.

### Async

```text
Task decides when to pause → await
```

### Multithreading

```text
Operating system decides when to switch threads
```

---

# Practical rules

1. `async def` creates a coroutine function.
2. `await` executes and waits for async operations.
3. `asyncio.run()` starts the event loop.
4. `asyncio.create_task()` schedules coroutines.
5. `await asyncio.sleep()` is non-blocking.
6. `time.sleep()` is blocking.
7. `asyncio.gather()` runs multiple coroutines concurrently.

---

# Quick summary

- Synchronous code runs step by step and blocks while waiting.
- Async code can pause at `await`, letting other work continue.
- Async is ideal when your program spends a lot of time waiting for I/O.
- Multithreading uses multiple threads, while async uses one thread and one event loop.

---

# Practice idea

When reading async code, watch for these patterns:

- `async def`
- `await`
- `asyncio.run(...)`
- `asyncio.create_task(...)`
- `asyncio.gather(...)`

Once you understand these patterns, you understand most real-world Python async code.