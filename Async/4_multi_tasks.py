import asyncio
import time

async def api_call(url:str,delay:int):
    print(f"Fetcing Data from {url}...")
    await asyncio.sleep(delay)
    print(f"Data Fetched from {url}...")

async def execute():
    time.sleep(4)
    print("Execution Completed...")
async def transform():
    asyncio.sleep(3)
    print("Transformation Completed...")

async def main():
    taks = await asyncio.gather(
        api_call("https://api.com",3), #here thread is not idle, it can do other tasks in the meantime while waiting for the API call to complete. and once the API call is completed, it will return the result.
        execute(), # here thread is idle for 4 seconds, meaning that nothing else can happen during this time.
        transform() # here thread wil not wait  for 3 seconds, it will just create a coroutine that will sleep for 3 seconds when awaited. so transform() will return a coroutine object immediately, in that scenario we need to use await to actually wait for the result of the coroutine.
    )
    print("All tasks completed.")
asyncio.run(main())