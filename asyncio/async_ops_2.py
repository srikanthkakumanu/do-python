import asyncio
import time


# subroutine i.e. without async/await, it will block the main thread until it finishes
def brew_coffee():
    print("Sync - Brewing coffee...")
    time.sleep(3)
    print("Sync - Coffee is ready!")
    return "Sync - Coffee Ready!"


# subroutine i.e. without async/await, it will block the main thread until it finishes
def toast_bread():
    print("Sync - Toasting bread...")
    time.sleep(2)
    print("Sync - Bread is toasted!")
    return "Sync - Toasted Bread Ready!"


def syncher():
    start_time = time.time()
    result_coffee = brew_coffee()
    result_bread = toast_bread()
    end_time = time.time()

    elapsed_time = end_time - start_time

    print(f"Sync - Coffee: {result_coffee}, Bread: {result_bread}")
    print(f"Sync - Total time taken: {elapsed_time:.2f} seconds")
    print("-" * 50)


# coroutine i.e. with async/await, it allows other tasks to run while waiting for the current task to finish
async def async_brew_coffee():
    print("Async - Start brewCoffee()")
    # normal sleep function is not awaitable, hence the asyncio.sleep() is used which is awaitable and allows other tasks to run while waiting
    # await time.sleep(3)
    await asyncio.sleep(3)
    print("Async - End brewCoffee()")
    return "Async - Coffee Ready!"


# coroutine i.e. with async/await, it allows other tasks to run while waiting for the current task to finish
async def async_toast_bread():
    print("Async - Start toastBread()")
    # normal sleep function is not awaitable, hence the asyncio.sleep() is used which is awaitable and allows other tasks to run while waiting
    # await time.sleep(2)
    await asyncio.sleep(2)
    print("Async - End toastBread()")
    return "Async - Toasted Bread Ready!"


async def asyncher_batch():
    start_time = time.time()

    # gather is used to run multiple coroutines concurrently in a batch and wait for them to finish
    batch = asyncio.gather(async_brew_coffee(), async_toast_bread())
    result_coffee, result_bread = await batch

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Async Batch - Coffee: {result_coffee}, Bread: {result_bread}")
    print(f"Async Batch - Total time taken: {elapsed_time:.2f} seconds")
    print("-" * 50)


async def asyncher_task():
    start_time = time.time()

    coffee_task = asyncio.create_task(async_brew_coffee())
    bread_task = asyncio.create_task(async_toast_bread())

    # create_task is used to create a task from a coroutine and schedule it to run concurrently, it returns a Task object which can be awaited to get the result of the coroutine
    result_coffee = await coffee_task
    result_bread = await bread_task

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Async Task - Coffee: {result_coffee}, Bread: {result_bread}")
    print(f"Async Task - Total time taken: {elapsed_time:.2f} seconds")
    print("-" * 50)


def main():
    syncher()
    asyncio.run(asyncher_batch())
    asyncio.run(asyncher_task())


if __name__ == "__main__":
    main()
    print(f"Is brew_coffee() a coroutine: {asyncio.iscoroutinefunction(brew_coffee)}")
    print(f"Is toast_bread() a coroutine: {asyncio.iscoroutinefunction(toast_bread)}")
    print(
        f"Is async_brew_coffee() a coroutine: {asyncio.iscoroutinefunction(async_brew_coffee)}"
    )
    print(
        f"Is async_toast_bread() a coroutine: {asyncio.iscoroutinefunction(async_toast_bread)}"
    )
    print(
        f"Is asyncher_batch() a coroutine: {asyncio.iscoroutinefunction(asyncher_batch)}"
    )
    print(
        f"Is asyncher_task() a coroutine: {asyncio.iscoroutinefunction(asyncher_task)}"
    )
