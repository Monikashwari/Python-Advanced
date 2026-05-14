import asyncio

async def api_call(url:str,delay:int):
    print(f"Fetcing Data from {url}...")
    await asyncio.sleep(delay)
    print(f"Data Fetched from {url}...")
    return f"Data from {url}"

async def main():
    tasks= await asyncio.gather(
        api_call("https://api1_1.com",6),
        api_call("https://api2_1.com",5),
        api_call("https://api3_1.com",4) 
    ) #here thread is not idle, it can do other tasks in the meantime while waiting for the API calls to complete. and once all the API calls are completed, it will return a list of results in the same order as the tasks were passed to gather.
    print("All tasks completed.")
    #another way to user gather method in list comprehension
    urls = [api_call(url,delay) for url,delay in [("https://api1.com",3),("https://api2.com",2),("https://api3.com",1)]]
    res = await asyncio.gather(*urls) 
    print("All tasks completed.")
asyncio.run(main())
    