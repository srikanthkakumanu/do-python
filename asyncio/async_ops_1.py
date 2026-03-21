# This example shows synchronous code execution,
import asyncio
import time


# coroutine
async def fetch_data(param):
    print(f"Do something with {param}...")
    await asyncio.sleep(param)  # Simulate a time-consuming operation
    print(f"Done with {param}")
    return f"Result of {param}"


# coroutine
async def main():
    task1 = fetch_data(1)  # could be awaited directly
    task2 = fetch_data(2)  # could be awaited directly
    result1 = await task1
    print("Task 1 fully completed")
    result2 = await task2
    print("Task 2 fully completed")
    return [result1, result2]


t1 = time.perf_counter()
results = asyncio.run(main())  # creates and runs in an event loop
print(results)
t2 = time.perf_counter()
print(f"Finished in {t2 - t1:.2f} seconds")
