# Concurrency in Python

<div class="style=justify;">

Python supports **co-operative concurrency**. `asyncio` is Python's built-in library to write concurrent code using `async`/`await` syntax. High-level building blocks of asyncio: **the event loop, coroutine functions, coroutine objects, tasks, and await**.

## Concurrency vs Parallelism

| **Concept** | **Concurrency** | **Parallelism** |
| --- | --- | --- |
| **Definition** | Multiple tasks in progress at the same time | Multiple tasks executing at the same time |
| **Focus** | Task management, scheduling, responsiveness | Speed, throughput, raw performance |
| **Requires multiple CPUs?** | No | Yes |
| **Example analogy** | One chef juggling many dishes | Many chefs cooking dishes simultaneously |
| **Primary goal** | Structure, responsiveness, avoiding blocking | Faster execution by dividing work |
| **Typical use cases** | Servers handling many requests, async I/O | CPU-bound workloads, ML training, batch processing |
| **Programming model** | async/await, event loops, coroutines | Threads, multiprocessing, SIMD, GPU kernels |


## Execution model

**Multithreading**: Multiple threads share the same memory space, but only one thread runs at a time in Python (because of the GIL). It is good for I/O-bound tasks.

**Multiprocessing**: Multiple processes, each with its own memory and Python interpreter. It gives true parallelism. It is good for CPU-bound tasks.

**Asyncio**: **Single thread, single process**. It uses an **event loop** to run many tasks concurrently by switching between them when one task is waiting (for example, waiting for network or file I/O). It is best for I/O-bound workloads along with high-concurrency workloads.



## Memory and overhead

**Threads**: Light, but still need stack memory.
**Processes**: Heavy, separate memory, higher overhead.
**Coroutines (asyncio)**: Ultra-light. Thousands of coroutines can run inside one thread because they do not need OS threads.

**Rule of thumb:**

- If the need is parallelism, use multiprocessing (for example, image/video processing).
- If the need is to handle blocking I/O with limited concurrency, use threads.
- If the need is to handle huge concurrency with I/O, use asyncio (for example, chat servers, web scraping, APIs).

## Threads vs Coroutines

| **Concept** | **Thread** | **Coroutine** |
| --- | --- | --- |
| **Scheduling** | Scheduling is done by the OS, so the **context switches** are **expensive**. | Scheduling is done by the **event loop** (Python-level), so the switching is **cheap** because it is just jumping between Python functions.|
| **Blocking vs Unblocking** | A thread can block (for example, `time.sleep(5)` blocks it). | A coroutine must use `await asyncio.sleep(5)` which pauses only that coroutine, not the whole thread. |
| **Paralallism** | In Python, there is no true parallel execution of Python code due to GIL. | No parallel execution. Just **cooperative multitasking**. Each coroutine yields control explicitly with `await`.Yes |

## Event Loop

Event Loop is a kind of scheduler that manages and runs asynchronous tasks, events/callbacks and I/O operations.

- Keeps track of all the tasks that are ready to run.
- Pauses tasks when they are waiting for something (like network data).
- Resumes them when the awaited operation is complete.
- **Single-threaded**: The loop runs in one thread but can handle thousands of concurrent I/O-bound tasks.
- **Best for**: Network requests, file I/O, timers — not CPU-heavy work.

### Event Loop Flow:

- **Start the loop** — The event loop runs continuously until all scheduled tasks are complete.
- **Register tasks** — You schedule coroutines (async def functions) or callbacks to run.
- **Non-blocking execution** — When a task hits an await (e.g., waiting for I/O), the loop switches to another task instead of blocking.
- **Completion** — The loop stops when there’s nothing left to do.

## Coroutine

A special function defined with `async def` that can be paused and resumed.  A coroutine represents the function’s body or logic. A coroutine has to be explicitly started; again, merely creating the coroutine does not start it `await` pauses execution until the awaited coroutine or task completes.

- Asynchronous function in Python is called a **coroutine**.
- Coroutines are declared with async/await keywords.
- Coroutines are special functions that return coroutine objects when called.

### Async Gather

`asyncio.gather()` runs tasks **concurrently** in batch fashion and waits for them to complete.

```python
import asyncio

batch = asyncio.gather(async_brew_coffee(), async_toast_bread())
result_coffee, result_bread = await batch
```

### Async Tasks

`asyncio.create_task()` creates a task from a coroutine and schedules it to run concurrently.

**Tasks use futures under the hood**. Therefore, we should use tasks instead of futures as futures are much lower level.

```python
import asyncio

coffee_task = asyncio.create_task(async_brew_coffee())
    bread_task = asyncio.create_task(async_toast_bread())

    # create_task is used to create a task from a coroutine and schedule it to run concurrently, it returns a Task object which can be awaited to get the result of the coroutine
    result_coffee = await coffee_task
    result_bread = await bread_task
```


</div>