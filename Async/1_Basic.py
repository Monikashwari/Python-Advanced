import asyncio
import time

def main():
    print("Hello")
    time.sleep(5) # This will block the entire thread for 5 seconds, meaning that nothing else can happen during this time.
    print("World")

async def two():
    print("Hello")
    await asyncio.sleep(5) # This will actually wait for 5 seconds before proceeding to the next line. but thread is not idle, it can do other tasks in the meantime.
    print("World")
async def one():
    print("One")
    asyncio.sleep(2) # This will not actually wait, it just creates a coroutine that will sleep for 2 seconds when awaited. 
    #if you use time instead of asyncio then it will be considered as a synchronous function.
    print("One done")
while True:
    print("Select the main function to run...")
    print("1. Synchronous") 
    print("2. Asynchronous with wait time")
    print("3. Asynchronous without wait time")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
      main()
    elif choice == 2:
      asyncio.run(two())
    elif choice == 3:
      asyncio.run(one())
    elif choice == 4:
      print("Exiting...")
      break
    else:
      print("Invalid choice.")