import time
import asyncio

def api_call_sync():
    time.sleep(3) # thread is idle for 3 seconds, meaning that nothing else can happen during this time.
    return "Revenue Data..."
def sync_main():
    print("Starting synchronous API call...")
    result = api_call_sync()
    print("Data Fetched :",result)

async def api_call_async_without_await():
    await asyncio.sleep(3)
    return "Revenue Data..."
async def async_main_without_await():
    print("Starting asynchronous API call...")
    result = api_call_async_without_await() # This will not actually wait, it just creates a coroutine that will sleep for 3 seconds when awaited. so api_call_async() will return a coroutine object immediately, in that scenario we need to use await to actually wait for the result of the coroutine.
    print("Data Fetched :",result)

async def api_call_async_with_await():
    await asyncio.sleep(3)
    return "Revenue Data..."
async def async_main_with_await():
    print("Starting asynchronous API call...")
    result = await api_call_async_with_await() # This will actually wait for 3 seconds before proceeding to the next line. but thread is not idle, it can do other tasks in the meantime.
    print("Data Fetched :",result)
while True:
    print("Select the main function to run...")
    print("1. Synchronous API Call") 
    print("2. Asynchronous API Call without await")
    print("3. Asynchronous API Call with await")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
      sync_main()
    elif choice == 2:
      asyncio.run(async_main_without_await())
    elif choice == 3:
      asyncio.run(async_main_with_await())
    elif choice == 4:
      print("Exiting...")
      break
    else:
      print("Invalid choice.")   